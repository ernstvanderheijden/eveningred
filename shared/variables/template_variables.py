def add_variables(request):
    context = {
        'username': "test_user_name_" + str(request.user.id),
    }
    if request.user.is_superuser:
        context.update({'show_ctx': True})
    return context
