import datetime
import io
import csv
import xlsxwriter
from django.contrib import messages
from django.db.models import Value, CharField, F
from django.db.models.functions import Concat
from django.http import HttpResponse
from django.shortcuts import redirect


def collect_data_exportlist_hours_or_materials(request, records, modelname):
    amountrecs = records.count()
    if amountrecs > 0:
        if modelname == 'Hour':
            records = getfields_hours(records)
            return records
        elif modelname == 'Material':
            records = getfields_materials(records)
            return records
        else:
            return None
    else:
        return None


def getfields_hours(records):
    records = records.annotate(fullname=Concat('userid__first_name', Value(' '), 'userid__insertion', Value(' '), 'userid__last_name', output_field=CharField()),
                               creator=Concat('creatorid__first_name', Value(' '), 'creatorid__insertion', Value(' '), 'creatorid__last_name', output_field=CharField()),
                               updater=Concat('updaterid__first_name', Value(' '), 'updaterid__insertion', Value(' '), 'updaterid__last_name', output_field=CharField()),
                               )
    records = records.values(ID=F('id'),
                             Medewerker=F('fullname'),
                             Omschrijving=F('description'),
                             Project=F('projectid__description'),
                             Datum=F('issuedate'),
                             Aantal=F('amounthours'),
                             Verwerkdatum=F('processdate'),
                             Aanmaakdatum=F('created'),
                             Updatedatum=F('updated'),
                             Aanmaker=F('creator'),
                             Updater=F('updater'),
                             )
    records = records.order_by('issuedate', 'fullname')
    return records


def getfields_materials(records):
    records = records.annotate(fullname=Concat('userid__first_name', Value(' '), 'userid__insertion', Value(' '), 'userid__last_name', output_field=CharField()),
                               creator=Concat('creatorid__first_name', Value(' '), 'creatorid__insertion', Value(' '), 'creatorid__last_name', output_field=CharField()),
                               updater=Concat('updaterid__first_name', Value(' '), 'updaterid__insertion', Value(' '), 'updaterid__last_name', output_field=CharField()),
                               )
    records = records.values(ID=F('id'),
                             Medewerker=F('fullname'),
                             Omschrijving=F('description'),
                             Project=F('projectid__description'),
                             Klant=F('customerid__relationname'),
                             Datum=F('issuedate'),
                             Inkoopkosten=F('purchasingcosts'),
                             Verwerkdatum=F('processdate'),
                             Aanmaakdatum=F('created'),
                             Updatedatum=F('updated'),
                             Aanmaker=F('creator'),
                             Updater=F('updater'),
                             )
    records = records.order_by('issuedate', 'fullname')
    return records


def export_list_csv_hours_or_materials(request, records, modelname):
    rows = collect_data_exportlist_hours_or_materials(request, records, modelname)

    if rows:
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=' + format(datetime.datetime.now(), "%Y%m%d%H%M%S") + "_" + modelname + ".csv"
        writer = csv.writer(response, delimiter=',')
        if modelname == 'Hour':
            columns = ['ID',
                       'Medewerker',
                       'Omschrijving',
                       'Project',
                       'Datum',
                       'Aantal',
                       'Verwerkdatum',
                       'Aanmaakdatum',
                       'Updatedatum=',
                       'Aanmaker',
                       'Updater']
        else:
            columns = ['ID',
                       'Medewerker',
                       'Omschrijving',
                       'Project',
                       'Klant',
                       'Datum',
                       'Inkoopkosten',
                       'Verwerkdatum',
                       'Aanmaakdatum',
                       'Updatedatum=',
                       'Aanmaker',
                       'Updater']
        writer.writerow(columns)

        for row in rows:
            writer.writerow(row.values())

        # Save the Now to the processdate
        records.update(processdate=datetime.datetime.now())

        return response
    else:
        return HttpResponse("Niets gevonden om te exporteren naar csv-file")


def export_list_xlsx_hours_or_materials(request, records, modelname):
    # Dataset must always be a query (.values)
    rows = collect_data_exportlist_hours_or_materials(request, records, modelname)

    if rows:
        pass
    else:
        messages.success(request, "Niet verwerkt")
        return redirect('/administration/process')

    # Create an in-memory output file for the new workbook.
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output, {'default_date_format': 'dd-mm-yyyy hh:mm'})
    worksheet = workbook.add_worksheet('Diensten')

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})
    row_num = 0

    if rows:
        if modelname == 'Hour':
            columns = ['ID',
                       'Medewerker',
                       'Omschrijving',
                       'Project',
                       'Datum',
                       'Aantal',
                       'Verwerkdatum',
                       'Aanmaakdatum',
                       'Updatedatum=',
                       'Aanmaker',
                       'Updater']
        else:
            columns = ['ID',
                       'Medewerker',
                       'Omschrijving',
                       'Project',
                       'Klant',
                       'Datum',
                       'Inkoopkosten',
                       'Verwerkdatum',
                       'Aanmaakdatum',
                       'Updatedatum=',
                       'Aanmaker',
                       'Updater']
        for col_num in range(len(columns)):
            worksheet.write(row_num, col_num, columns[col_num], bold)

        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                worksheet.write(row_num, col_num, row[list(row)[col_num]])

        # Close the workbook before sending the data.
        workbook.close()

        # Rewind the buffer.
        output.seek(0)

        # Set up the Http response.
        filename = format(datetime.datetime.now(), "%Y%m%d%H%M%S") + "_" + modelname + ".xlsx"
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename

        # Save the Now to the processdate
        records.update(processdate=datetime.datetime.now())

        return response
    else:
        return HttpResponse("Niets gevonden om te exporteren naar xlsx-file.")
