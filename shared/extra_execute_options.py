# from invoices.models import Invoice
from shared.functions import fill_data_with_print_records
# from shared.invoice import finalize_invoice, send_invoices


def add_extra_execute_options(self, record):
    match self.ctx['package']:
        case 'invoices':
            if record.__class__.__name__ == "Invoice":
                if self.request.GET.get('finalize', '') == 'true':
                    pass
                    # record = Invoice.objects.get(id=record.id)
                    # record = finalize_invoice(record)
                    # records = Invoice.objects.filter(id=record.id)
                    # response = send_invoices(records)
                    # if isinstance(response, str):
                    #     self.data['messagelist'] = ["Facturen verzonden, geen facturen te printen", "success", "long"]
                    #     self.data['form_is_valid'] = True
                    # elif isinstance(response, list):
                    #     fill_data_with_print_records(self.data, response)
    return
