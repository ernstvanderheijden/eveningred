def set_moduledata(request):
    moduledata = list()

    moduledata.append({
        "Dashboard": {
            "url": "/",
            "icon": "bi bi-columns-gap"
        },
    })


    if request.user.has_perm('relations.view_relation'):
        moduledata.append({
            "Relatiebeheer": {
                "url": "/core/template/?level=0&package=relations&chapter=list",
                "icon": "bi bi-building",
            },
        })

    if request.user.has_perm('projects.view_project'):
        moduledata.append({
            "Projectbeheer": {
                "url": "/core/template/?level=0&package=projects&chapter=list",
                "icon": "bi bi-house-door",
            },
        })

    if request.user.has_perm('hours.view_hour'):
        moduledata.append({
            "Mijn urenbeheer": {
                "url": "/core/template/?level=0&package=hours&chapter=list",
                "icon": "bi bi-stopwatch",
            },
        })

    if request.user.has_perm('materials.view_material'):
        moduledata.append({
            "Mijn materiaalbeheer": {
                "url": "/core/template/?level=0&package=materials&chapter=list",
                "icon": "bi bi-boxes",
            },
        })

    if request.user.has_perm('projects.process_project'):
        moduledata.append({
            "Overzichten": {
                "url": "/core/template/?level=0&package=overviews&chapter=overviewhours",
                "icon": "bi bi-calendar4-range",
            },
        })

    if request.user.has_perm('articles.view_article'):
        moduledata.append({
            "Artikelbeheer": {
                "url": "/core/template/?level=0&package=articles&chapter=list",
                "icon": "bi bi-cart2",
                "seperator": True
            },
        })

    if request.user.has_perm('users.view_user'):
        moduledata.append({
            "Gebruikersbeheer": {
                "url": "/core/template/?level=0&package=users&chapter=list",
                "icon": "bi bi-people",
            },
        })

    if request.user.has_perm('master.view_articlegroup'):
        moduledata.append({
            "Stamgegevens": {
                "url": "/core/template/?level=0&package=master&chapter=listarticlegroup",
                "icon": "bi bi-wrench"
            },
        })

    if request.user.has_perm('emails.view_email'):
        moduledata.append({
            "Verzonden mail": {
                "url": "/core/template/?level=0&package=emails&chapter=list",
                "icon": "bi bi-envelope",
            },
        })

    if request.user.has_perm('applog.view_applog'):
        moduledata.append({
            "Logboek": {
                "url": "/core/template/?level=0&package=applog&chapter=list",
                "icon": "bi bi-card-list",
            },
        })

    if request.user.has_perm('configuration.view_configuration'):
        moduledata.append({
            "Instellingen": {
                "url": "/core/template/?level=0&package=configuration&chapter=list",
                "icon": "bi bi-sliders",
            },
        })

    return moduledata
