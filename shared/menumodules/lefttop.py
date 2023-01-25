def set_moduledata(request):
    moduledata = list()

    moduledata.append({
        "Dashboard": {
            "url": "/",
            "icon": "bi bi-columns-gap"
        },
    })

    if request.user.is_employee:
        moduledata.append({
            "Relatiebeheer": {
                "url": "/core/template/?level=0&package=relations&chapter=list",
                "icon": "bi bi-building",
            },
        })

    if request.user.is_employee:
        moduledata.append({
            "Artikelbeheer": {
                "url": "/core/template/?level=0&package=articles&chapter=list",
                "icon": "bi bi-cart2",
                "seperator": True
            },
        })

    if request.user.is_employee:
        moduledata.append({
            "Gebruikersbeheer": {
                "url": "/core/template/?level=0&package=users&chapter=list",
                "icon": "bi bi-people",
            },
        })

    if request.user.is_employee:
        moduledata.append({
            "Stamgegevens": {
                "url": "/core/template/?level=0&package=master&chapter=listarticlegroup",
                "icon": "bi bi-wrench"
            },
        })

    if request.user.is_employee:
        moduledata.append({
            "Verzonden mail": {
                "url": "/core/template/?level=0&package=emails&chapter=list",
                "icon": "bi bi-envelope",
            },
        })

    if request.user.is_employee:
        moduledata.append({
            "Logboek": {
                "url": "/core/template/?level=0&package=applog&chapter=list",
                "icon": "bi bi-card-list",
            },
        })

    if request.user.is_employee:
        moduledata.append({
            "Instellingen": {
                "url": "/core/template/?level=0&package=configuration&chapter=list",
                "icon": "bi bi-sliders",
            },
        })

    return moduledata
