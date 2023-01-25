from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from core.middleware import local
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from core.tokens import url_one_job_token
from emails.models import Email
from tenants.models import Domain


def send_email(on_trial, ctx, html_message, plain_message):
    #  Mind out: Always fill ctx['cc_email'] en ctx['bcc_email'] as list []
    if on_trial:  # In Tenants at public schema the field 'on_trial' must be false to send mails, except for the activation email
        print("Tenant is on_trial (Tenant.on_trial = True), so no email will be send")
    else:
        msg = EmailMultiAlternatives(subject=ctx['mail_subject'],
                                     body=plain_message,
                                     from_email=ctx['from_email'],
                                     to=ctx['to_email'],
                                     cc=ctx['cc_email'],
                                     bcc=ctx['bcc_email'],
                                     attachments=ctx['attachments'],
                                     reply_to=[ctx['reply_to']])
        if 'pdfobject' in ctx:
            msg.attach(ctx['pdfobjectname'], ctx['pdfobject'])
        msg.attach_alternative(html_message, "text/html")
        msg.send()

    # Save the email in de database
    email = Email()
    if str(local.user) == 'AnonymousUser':
        from users.models import User
        user = User.objects.get(email=ctx['emailaddress'])
        email.user = user
    else:
        email.user = local.user
    email.status = 9
    email.to_email = ctx['to_email']
    email.cc_email = ctx['cc_email']
    email.bcc_email = ctx['bcc_email']
    email.from_email = ctx['from_email']
    email.reply_to = ctx['reply_to']
    email.mail_subject = ctx['mail_subject']
    email.plain_message = plain_message
    email.html_message = html_message
    email.attachments = ctx['attachments']
    email.save()
    return email


def create_ctx_email(to_email, ctx, attachments=None):
    if attachments is None:
        attachments = []
    from django.db import connection
    from configuration.models import Configuration
    cnf = Configuration.default.get()
    from relations.models import Relation
    rel = Relation.objects.get(is_master=True)
    tenant = Domain.objects.filter(tenant__schema_name=connection.schema_name).exclude(domain='localhost').values('domain', 'tenant_id', 'tenant__name', 'tenant__on_trial')[0]
    ctx['on_trial'] = tenant['tenant__on_trial']  # In Tenants at public schema the field 'on_trial' must be false to send mails, except for the activation email
    ctx['from_email'] = cnf.email_display_name + '<' + cnf.email_from + '>'
    ctx['reply_to'] = cnf.email_reply_to
    ctx['email_logo'] = cnf.email_logo
    ctx['to_email'] = to_email
    ctx['cc_email'] = []
    ctx['bcc_email'] = []
    ctx['attachments'] = attachments

    ctx['tenant_name'] = tenant['tenant__name']
    ctx['domain_url'] = tenant['domain']

    ctx['sender_relationname'] = rel.relationname
    ctx['sender_fulladdress'] = rel.fulladdress
    ctx['sender_phone'] = rel.phone
    ctx['sender_email'] = rel.email
    ctx['sender_homepage'] = cnf.homepage
    ctx['sender_aboutuspage'] = cnf.aboutuspage
    ctx['sender_contactpage'] = cnf.contactpage
    ctx['sender_instagrampage'] = cnf.instagrampage
    ctx['sender_facebookpage'] = cnf.facebookpage


# def create_email_slug_invoice(invoice, to_email, salutation, ctx, attachments=None):
#     create_ctx_email(to_email, ctx, attachments=None)
#
#     ctx['salutation'] = salutation
#     ctx['mail_subject'] = "Factuur " + invoice.invoicenumber
#     ctx['introduction'] = render_to_string('shared/email/introductions/invoice.html', {'ctx': ctx, 'record': invoice})
#     ctx['action_url'] = "public/invoice/" + invoice.slug
#     ctx['action_title'] = "Open factuur"
#
#     # Create body for e-email in html and in plain text
#     html_message = render_to_string('shared/email/base/base.html', {'ctx': ctx, 'record': invoice})
#     plain_message = strip_tags(render_to_string('shared/email/base/plain.html', {'ctx': ctx, 'record': invoice}))
#     email = send_email(ctx['on_trial'], ctx, html_message, plain_message)
#     return email
#
#
# def create_email_invoice_pdf_to_accountancy(invoice, to_email, salutation, ctx, pdfobject):
#     create_ctx_email(to_email, ctx, attachments=None)
#
#     ctx['salutation'] = salutation
#     ctx['mail_subject'] = "[VRK] Verkoopfactuur " + str(invoice.invoicenumber)
#     ctx['introduction'] = "In de bijlage treft u een nieuwe verkoopfactuur aan."
#     ctx['action_url'] = ""
#     ctx['action_title'] = ""
#     ctx['pdfobject'] = pdfobject
#     ctx['pdfobjectname'] = "Factuur " + str(invoice.invoicenumber) + ".pdf"
#
#     # Create body for e-email in html and in plain text
#     html_message = render_to_string('shared/email/base/base.html', {'ctx': ctx, 'record': invoice})
#     plain_message = strip_tags(render_to_string('shared/email/base/plain.html', {'ctx': ctx, 'record': invoice}))
#     email = send_email(ctx['on_trial'], ctx, html_message, plain_message)
#     return email
#
#
# def create_email_slug_contract(contract, to_email, salutation, ctx, attachments=None):
#     create_ctx_email(to_email, ctx, attachments=None)
#
#     ctx['salutation'] = salutation
#     ctx['mail_subject'] = "Reservering " + contract.contractnumber
#     ctx['introduction'] = render_to_string('shared/email/introductions/contract.html', {'ctx': ctx, 'record': contract})
#     ctx['action_url'] = "public/contract/agree/" + contract.slug
#     ctx['action_title'] = "Open contract"
#
#     # Create body for e-email in html and in plain text
#     html_message = render_to_string('shared/email/base/base.html', {'ctx': ctx, 'record': contract})
#     plain_message = strip_tags(render_to_string('shared/email/base/plain.html', {'ctx': ctx, 'record': contract}))
#     email = send_email(ctx['on_trial'], ctx, html_message, plain_message)
#     return email


def create_email_user_invitation(user, to_email, salutation, ctx, attachments=None):
    create_ctx_email(to_email, ctx, attachments=None)

    ctx['salutation'] = salutation
    ctx['mail_subject'] = "Wachtwoord instellen"

    ctx['uid'] = urlsafe_base64_encode(force_bytes(user.id))
    ctx['token'] = url_one_job_token.make_token(user)

    ctx['username'] = user.username
    ctx['introduction'] = render_to_string('shared/email/introductions/invite.html', {'ctx': ctx, 'record': user})
    ctx['action_url'] = "setpassword/" + ctx['uid'] + "/" + ctx['token']
    ctx['action_title'] = "Activeer je acount"

    # Create body for e-email in html and in plain text
    html_message = render_to_string('shared/email/base/base.html', {'ctx': ctx, 'record': user})
    plain_message = strip_tags(render_to_string('shared/email/base/plain.html', {'ctx': ctx, 'record': user}))
    email = send_email(ctx['on_trial'], ctx, html_message, plain_message)
    return email
