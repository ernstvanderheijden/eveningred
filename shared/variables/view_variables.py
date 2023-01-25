from users.models import User


def set_user_variables(request):
    if request.user.id:
        user = User.objects.get(id=request.user.id)

        request.session['user_name'] = "name_user_id_" + str(request.user.id)
        request.session['paginatesize'] = user.paginatesize
    else:
        request.session['user_name'] = "Gast"
        request.session['paginatesize'] = 10

    request.session['variables_loaded'] = True
    print("self.request.session['variables_loaded'] is set to", request.session['variables_loaded'], "for user: ", request.session['user_name'])
