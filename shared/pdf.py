from io import BytesIO
import os
# from math import fsum

from django.conf import settings
# from django.db import connection
# from django.db.models import Sum
from django.http import HttpResponse
from django.template.loader import render_to_string

# from contracts.models import Contractline
# from invoices.models import Invoiceline
from pikepdf import Pdf
from xhtml2pdf import pisa

from shared.applog import get_applog_records_for_contract


# from shared.packages.contracts.crudagree import Crudagree


def render_to_pdf(template_name, context):
    html = render_to_string(template_name, context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return result
    return None


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    surl = settings.STATIC_URL  # Typically /static/
    sroot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
    murl = settings.MEDIA_URL  # Typically /static/media/
    mroot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(murl):
        path = os.path.join(mroot, uri.replace(murl, ""))
    elif uri.startswith(surl):
        path = os.path.join(sroot, uri.replace(surl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (surl, murl)
        )
    return path


def create_pdf_from_ctx(pdf, ctx):
    result = render_to_pdf(ctx['template_name'], {'ctx': ctx})
    if result:
        with Pdf.open(result) as resultpdf:
            pdf.pages.extend(resultpdf.pages)
    return pdf


def download_or_open_pdf(pdf, strtype, filename):
    if pdf:
        pdf_in_bytes = BytesIO()
        pdf.save(pdf_in_bytes)
        pdf.close()
        match strtype:
            case 'download':
                response = HttpResponse(pdf_in_bytes.getvalue(), content_type='application/force-download')
                response['Content-Disposition'] = 'inline; filename=' + filename
                return response
            case 'open':
                response = HttpResponse(pdf_in_bytes.getvalue(), content_type='application/pdf')
                response['Content-Disposition'] = 'inline; filename=' + filename
                return response
            case 'pdf':
                return pdf_in_bytes.getvalue()
    return None
