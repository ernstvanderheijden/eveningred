from pydoc import locate

from django.apps import apps


def update_record(request, pk):
    record = {}
    package = request.GET.get('package', '')
    try:
        if package:
            nameform = request.GET.get('nameform')
            modulepath = 'shared.packages.' + package.lower() + '.forms.' + nameform
            modelname = getattr(locate(modulepath), 'modelname')
            model = apps.get_model(package.lower(), modelname)
            """ Get the record"""
            record = model.objects.get(id=pk)
    except KeyError as e:
        print("Keyerror, no data passed update, missing:", e)
    return record
