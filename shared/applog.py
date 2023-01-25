from django.db.models import Q

from applog.models import Applog


def get_applog_records_for_contract(pk):
    # Applog for mutations on contract
    records = Applog.objects.filter(
        Q(app_name='contracts', model_name='contract', model_id=pk),
        (
                Q(reason='field_update', messagetype='mutation') |
                Q(reason='agreed')
        )
    )
    records = records.values('message', 'created', 'reason', 'messagetype')
    records = records.order_by('created')
    return records
