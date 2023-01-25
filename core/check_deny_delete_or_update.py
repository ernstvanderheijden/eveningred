from django.apps import apps


def check_deny_del_or_upd(pk, models_link_dictionary):
    for package, data in models_link_dictionary.items():
        strpackage = data['package'].lower()
        modelname = data['model'].title()
        namefield = data['namefield'].lower()
        model = apps.get_model(strpackage, modelname)
        if 'extra_filter' in data:
            cntr = model.objects.filter(**{namefield: pk}, **data['extra_filter']).count()
        else:
            cntr = model.objects.filter(**{namefield: pk}).count()
        if cntr > 0:
            return True
    return False
