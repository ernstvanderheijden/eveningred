from django import forms
from pydoc import locate
from django.apps import apps
from django.forms import inlineformset_factory

MODEL = None
MODELCHILD = None


def define_meta_model(model):
    global MODEL
    MODEL = model


def define_meta_model_child(modelchild):
    global MODELCHILD
    MODELCHILD = modelchild


def make_form_class(*args, **kwargs):
    class GlobalForm(forms.ModelForm):
        class Meta:
            model = MODEL
            fields = '__all__'
    return GlobalForm(*args, **kwargs)


def set_form(request, package, record):
    nameform = request.GET.get('nameform')
    fk = request.GET.get('fk', '')

    if fk:  # Get the name of the package to crud with
        modulepath = 'shared.packages.' + package.lower() + '.forms.' + nameform  # Get variable in the custom form from package.py
    else:
        modulepath = 'shared.packages.' + package.lower() + '.base.basepackage'  # Get variable package from package.py
    package = getattr(locate(modulepath), 'packagename')

    modulepath = 'shared.packages.' + package.lower() + '.forms.' + nameform  # Get the name of the model
    modelname = getattr(locate(modulepath), 'modelname')
    define_meta_model(apps.get_model(package.lower(), modelname))

    if record:
        if request.POST:
            form = make_form_class(request.POST, instance=record)
        else:
            form = make_form_class(instance=record)
    else:
        if request.POST:
            form = make_form_class(request.POST)
        else:
            form = make_form_class()
    return form


def set_formset(request, package, record, ctx):
    nameform = request.GET.get('nameform')
    modulepath = 'shared.packages.' + package.lower() + '.forms.' + nameform  # Get variable in the custom form from package.py
    package = getattr(locate(modulepath), 'packagename')
    modelname = getattr(locate(modulepath), 'modelname')

    packagechild = getattr(locate(modulepath), 'packagenamechild')
    modulepathchild = 'shared.packages.' + packagechild.lower() + '.forms.' + nameform  # Get the name of the model
    modelnamechild = getattr(locate(modulepathchild), 'modelnamechild')
    define_meta_model(apps.get_model(package.lower(), modelname))
    define_meta_model_child(apps.get_model(packagechild.lower(), modelnamechild))
    inlineformset = inlineformset_factory(MODEL, MODELCHILD, fields='__all__', extra=ctx['amount_extra_records'])
    if 'initial_values' in ctx:
        formset = inlineformset(instance=record, initial=ctx['initial_values'], queryset=ctx['records'])
    else:
        formset = inlineformset(instance=record, queryset=ctx['records'])
    # formset = inlineformset(queryset=MODELCHILD.objects.none(), instance=record)  # Don't show existing childs
    if request.POST:
        formset = inlineformset(request.POST, request.FILES, instance=record)
    return formset


def set_fieldlist(request, package):
    nameform = request.GET.get('nameform')
    modulepath = 'shared.packages.' + package.lower() + '.forms.' + nameform
    nameform = getattr(locate(modulepath), nameform.title())
    return vars(nameform(request))
