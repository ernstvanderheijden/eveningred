from django import template
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from tenants.models import Version

register = template.Library()


@register.simple_tag
def define(val=None):
    return val


@register.simple_tag
def static_version():
    version = Version.objects.get().static_version
    return version


@register.simple_tag
def get_fieldtype_columnfield(columnfields, field):
    return columnfields[field]['fieldtype']


@register.simple_tag
def get_default_value_columnfield(columnfields, field):
    if 'default_value' in columnfields[field]:
        return columnfields[field]['default_value']
    else:
        return ''


@register.simple_tag
def get_fieldcaption_columnfield(columnfields, field):
    return columnfields[field]['caption']


@register.simple_tag
def create_fieldid_from_fieldname(fieldname):
    return 'id_' + fieldname


@register.simple_tag
def get_choicelist_columnfield(columnfields, field):
    return columnfields[field]['choicelist']


@register.simple_tag
def get_mindate_columnfield(columnfields, field):
    return columnfields[field]['min']


@register.simple_tag
def get_maxdate_columnfield(columnfields, field):
    return columnfields[field]['max']


@register.simple_tag
def get_fk_package_columnfield(columnfields, field):
    return columnfields[field]['fk_package']


@register.simple_tag
def get_fk_chapter_columnfield(columnfields, field):
    return columnfields[field]['fk_chapter']


@register.simple_tag
def get_linkdescription_columnfield(columnfields, field):
    return columnfields[field]['linkdescription']


@register.simple_tag
def get_value_columnfield(columnfields, field):
    return columnfields[field]['value']


@register.simple_tag
def get_data_attrs(data_attrs):
    attrs = ""
    for key, value in data_attrs.items():
        attrs = attrs + key + "=" + str(value) + " "
    return attrs


@register.simple_tag
def get_templatename_columnfield(columnfields, field):
    return columnfields[field]['templatename']


@register.simple_tag
def get_applog_message(applogs):
    htmltext = ""
    for applog in applogs:
        match applog['messagetype']:
            case "sourcedata":
                match applog['reason']:
                    case 'agreed':
                        htmltext = htmltext + render_to_string('shared/tags/applog_sourcedata_reason.html', {'applog': applog})
            case "manual":
                match applog['reason']:
                    case 'agreed':
                        htmltext = htmltext + render_to_string('shared/tags/applog_sourcedata_reason.html', {'applog': applog})
            case "mutation":
                match applog['reason']:
                    case 'field_update':
                        htmltext = htmltext + render_to_string('shared/tags/applog_mutation_field_update.html', {'applog': applog})
    return mark_safe(htmltext)


@register.simple_tag
def set_value_decimal(value):
    # if value: todo dit kan zo niet
    # if type(value) != float:
    #     value = float(value.replace(",", "."))
    return value


@register.simple_tag
def create_list_from_value(value):
    if value:
        listvalue = value.replace("[", "").replace("'", "").replace('"', "").replace("]", "").split(",")
        return listvalue


@register.simple_tag
def get_amount_from_list(fieldvalue):
    if fieldvalue:
        return len(fieldvalue)
    else:
        return ""


@register.simple_tag
def replace_onclick_values(onclick, record, namefield):
    strdisplayfield = ''
    if namefield:
        strdisplayfield = record[namefield]
    if strdisplayfield:
        stronclick = onclick.replace("pk_replace", str(record['id'])).replace("displayfield_replace", strdisplayfield)
    else:
        stronclick = onclick.replace("pk_replace", str(record['id'])).replace("displayfield_replace", "no_displayfield_value")
    return stronclick


@register.simple_tag
def replace_choice_day_month_once(value):  # for replacing level_higher from module value to set the right level
    if value:
        return value.replace("day", "Per dag").replace("month", "Per maand").replace("once", "Eenmalig")
    else:
        return ''


@register.simple_tag
def replace_monthnumber(value):  # for replacing level_higher from module value to set the right level
    match value:
        case 1:
            return "januari"
        case 2:
            return "februari"
        case 3:
            return "maart"
        case 4:
            return "april"
        case 5:
            return "mei"
        case 6:
            return "juni"
        case 7:
            return "juli"
        case 8:
            return "augustus"
        case 9:
            return "september"
        case 10:
            return "oktober"
        case 11:
            return "november"
        case 12:
            return "december"
        case _:
            return ""


@register.simple_tag
def fill_status_choice(status):
    match status:
        case 0:
            return "Actief"
        case -1:
            return "Inactief"


@register.simple_tag
def fill_sendmethod_choice(status):
    match status:
        case 1:
            return mark_safe('<i class="far fa-envelope text-black-50"></i>')
        case 2:
            return mark_safe('<i class="fas fa-print text-black-50"></i>')


@register.simple_tag
def boolean_icon(value):
    match value:
        case True:
            return mark_safe('<i class="fas fa-check text-success"></i>')
        case False:
            return mark_safe('<i class="fas fa-times text-danger"></i>')
        case _:
            return mark_safe('<i class="fas fa-times text-danger"></i>')


@register.simple_tag
def boolean_text(value):
    match value:
        case True:
            return mark_safe('<span class="text-success">wel</span>')
        case False:
            return mark_safe('<span class="text-danger">niet</span>')
        case _:
            return mark_safe('<span class="text-danger">niet</span>')


@register.simple_tag
def boolean_icon_true(value):
    match value:
        case True:
            return mark_safe('<i class="fas fa-check text-success"></i>')
        case _:
            return mark_safe('')


@register.simple_tag
def boolean_yn(value):
    match value:
        case True:
            return "Ja"
        case False:
            return "Nee"
        case _:
            return "Onbepaald"


@register.simple_tag
def note_icon(severity):
    match severity:
        case "info":
            return mark_safe('<i class="fas fa-info text-info me-2"></i>')
        case "warning":
            return mark_safe('<i class="fas fa-info text-warning me-2"></i>')
        case "danger":
            return mark_safe('<i class="fas fa-exclamation-triangle text-danger me-2"></i>')


@register.simple_tag
def fill_status_period(status):
    match status:
        case 9:
            return "Gesloten"
        case 0:
            return "In behandeling"
        case "":
            return "Ontbreekt"


@register.simple_tag
def fill_status_process(status):
    match status:
        case 0:
            return "In behandeling"
        case 9:
            return "Uitgevoerd"


@register.simple_tag
def fill_status_contract(status):
    match status:
        case 0:
            return "Concept"
        case 5:
            return "Gereserveerd"
        case 10:
            return "Bevestigd"
        case 20:
            return "Ingecheckt"
        case 30:
            return "Uitgecheckt"
        case 50:
            return "Afgerond"
        case 99:
            return "Geannuleerd"


@register.simple_tag
def fill_status_mollie(status):
    match status:
        case 'geen':
            return "Geen"
        case 'open':
            return "Openstaand"
        case 'canceled':
            return "Geannuleerd"
        case 'pending':
            return "In behandeling"
        case 'authorized':
            return "Goedgekeurd"
        case 'expired':
            return "Verlopen"
        case 'failed':
            return "Mislukt"
        case 'paid':
            return "Betaald"


@register.simple_tag
def fill_status_invoice(status):
    match status:
        case -1:
            return "Leeg"
        case 0:
            return "Concept"
        case 9:
            return "Definitief"


@register.simple_tag
def fill_status_email(status):
    match status:
        case 0:
            return "Gereed voor verzenden"
        case 9:
            return "Verzonden"


@register.simple_tag
def fill_severity_choice(severity):
    match severity:
        case 5:
            return "Highest"
        case 4:
            return "High"
        case 3:
            return "Medium"
        case 2:
            return "Low"
        case 1:
            return "Lowest"


@register.simple_tag
def fill_idtype_choice(idtype):
    match idtype:
        case "passport":
            return "Paspoort"
        case 'driverslicense':
            return "Rijbewijs"
        case 'idcard':
            return "ID-kaart"
        case _:
            return ''


@register.filter
def subtract(value, arg):
    if value and arg:
        return int(value) - int(arg)
    else:
        return ''


@register.filter(name='get_fieldvalue')
def get_fieldvalue(value, key):
    if key:
        return getattr(value, key)
    else:
        return ''


@register.filter(name='level_higher')
def level_higher(level):
    level = int(level)
    return level + 1


@register.filter(name='level_lower')
def level_lower(level):
    level = int(level)
    return level - 1


@register.filter(name='space_to_underscore')
def space_to_underscore(value):
    return value.replace(" ", "_")


@register.filter(name='selectable_when')
def selectable_when(value, record):  # filter specialy to determine if selectmultiple can go through, see selectmultiple_when in modules
    if value:
        for key, keydata in value.items():
            if record[key] == keydata:
                return True
            else:
                return False
    else:
        return False


@register.filter(name='replace_level_higher')
def replace_level_higher(key, value):  # for replacing level_higher from module value to set the right level
    if key:
        return key.replace("level_higher", str(int(value) + 1))
    else:
        return ''


@register.filter(name='get_value_field_from_filterfieldvalue')
def get_value_field_from_filterfieldvalue(filterfieldvalue, namefield):
    if namefield in filterfieldvalue:
        return filterfieldvalue[namefield]
    else:
        return ''
