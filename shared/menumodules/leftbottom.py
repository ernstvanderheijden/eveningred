def set_moduledata(request):
    """ Testpage """
    moduledata = [{}]

    """ User menu """    """ Build Submenu's first """
    if request:
        sublist = list()
        # if request.user.is_staff or request.user.is_superuser:
        #     sublist.append({"Testpage": {"onclick": "menu_testpage1()", "icon": "layers", }, }, )
        # if request.user.is_staff or request.user.is_superuser:
        #     sublist.append({"Version up": {"onclick": "set_new_versionnr()", "icon": "upgrade", }, }, )
        # if request.user.is_staff or request.user.is_superuser:
        #     sublist.append({"Showctx": {"onclick": "setright_is_dev({{ request.user.id }})", "icon": "bug_report", }, }, )
        if request.user.is_staff or request.user.is_superuser:
            sublist.append({"Admin": {"url": "/admin", "icon": "", }, }, )
            # sublist.append({"Admin": {"onclick": "window.open('/admin/', '_blank')", "icon": "tune", }, }, )
        # if request.user.is_staff or request.user.is_superuser:
        #     sublist.append({"Releasenotes": {"onclick": "menu_releasenotes()", "icon": "new_releases", }, }, )
        if request.user.is_staff or request.user.is_superuser:
            sublist.append({"Wachtwoord": {"url": "/password", "icon": "", }, }, )
        if request.user.is_staff or request.user.is_superuser:
            sublist.append({"Uitloggen": {"url": "/logout", "icon": "", }, }, )

        """ Add Item + sublist to the list moduledata"""
        moduledata.append({"Gebruiker": {"submenu": sublist, "icon": ""}, })

    return moduledata
