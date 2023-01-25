# from django.contrib.auth.decorators import user_passes_test
# from django.contrib.auth import REDIRECT_FIELD_NAME


# def is_superuser_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Superuser
#     actual_decorator = user_passes_test(lambda u: u.is_superuser, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator


# def is_staff_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Configuration / Eigenaar Software data
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.is_staff, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator


# def is_manager_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Manager / Rapportage
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_man, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator


# def is_employee_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Master / Stamgegevens
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_employee, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator


# def is_man_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Manager / Rapportage
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_man, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator


# def is_staff_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Configuration / Eigenaar Software data
#     actual_decorator = user_passes_tenant_test(lambda u: u.is_staff, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator


# def is_conf_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Configuration / Eigenaar Software data
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_conf, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_conf_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Configuration / Eigenaar Software data
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_conf, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_art_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Article / Artikelen
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_art, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_art_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Article / Artikelen
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_art, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_employee_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Master / Stamgegevens
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_employee, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_employee_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Master / Stamgegevens
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_employee, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_usr_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # User / Professionals
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_usr, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_usr_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # User / Professionals
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_usr, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_hrm_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Master / Stamgegevens
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_hrm, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_hrm_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Master / Stamgegevens
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_hrm, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_adm_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Administratie
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_adm, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_adm_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Administratie
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_adm, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_prj_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Projecten
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_prj, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_prj_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Projecten
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_prj, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_rel_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Relaties
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_rel, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_rel_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Relaties
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_rel, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_ord_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Orders
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_ord, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_ord_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Orders
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_ord, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_qua_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Orders
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_qua, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_qua_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Orders
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_qua, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_doc_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Docbuilder
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_doc, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_doc_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Docbuilder
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_doc, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_rie_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # RIenE
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_rie, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_rie_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # RIenE
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_rie, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_ros_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Planboard / Planbord
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_ros, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_ros_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Planboard / Planbord
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_ros, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_coo_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Planboard / Planbord
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_coo, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_coo_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Planboard / Planbord
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_coo, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_shi_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Performer / Professional
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_shi, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_shi_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Performer / Professional
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_shi, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_acc_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Accounting / Factuurnummers
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_acc, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_acc_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Accounting / Factuurnummers
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_acc, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_tim_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Timesheet for external user / Urenstaat voor externe gebruiker
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_tim, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_tim_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Timesheet for external user / Urenstaat voor externe gebruiker
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_tim, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_dev_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Developer / Ontwikkelaar
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_dev, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_dev_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Developer / Ontwikkelaar
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_dev, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_asm_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Asito master / Asito stamgegevens
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_asm, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_asm_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Asito master / Asito stamgegevens
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_asm, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_asw_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Asito worklines / Asito werkregels
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_asw, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_asw_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Asito worklines / Asito werkregels
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_asw, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_asr_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Asito read / Asito leesrecht
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_asr, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_asr_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Asito read / Asito leesrecht
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_asr, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_asn_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Asito NS read / Asito NS leesrecht
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_asn, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_asn_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Asito NS read / Asito NS leesrecht
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_asn, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_wpr_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Workpraperation / Werkvoorbereiding
#     actual_decorator = user_passes_test(lambda u: u.is_active and u.rights.is_wpr, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator
#
#
# def is_wpr_public_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):  # Workpraperation / Werkvoorbereiding
#     actual_decorator = user_passes_public_test(lambda u: u.rights.is_wpr, login_url=login_url, redirect_field_name=redirect_field_name)
#     if function:
#         return actual_decorator(function)
#     return actual_decorator

