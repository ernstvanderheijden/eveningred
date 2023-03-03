def check_extra_delete_refusals(request, package, modelname, record):
    extra_delete_refusals = False
    match package:
        case 'configuration':
            if modelname == 'Configuration':
                if record.is_default:
                    extra_delete_refusals = True
        # case 'contracts':
        #     if modelname == 'Contract':
        #         if hasattr(record, 'status'):
        #             if record.status != 0:
        #                 extra_delete_refusals = True
        # case 'invoices':
        #     if modelname == 'Invoice':
        #         if hasattr(record, 'status'):
        #             if record.status != 0:
        #                 extra_delete_refusals = True
        case 'hours':
            # Can not delete master
            if modelname == 'Hour':
                if record.processdate:
                    extra_delete_refusals = True
        case 'materials':
            # Can not delete master
            if modelname == 'Material':
                if record.processdate:
                    extra_delete_refusals = True
        case 'relations':
            # Can not delete master
            if modelname == 'Relation':
                if record.is_master:
                    extra_delete_refusals = True
        case 'users':
            # Can not delete yourself
            if modelname == 'User':
                if record.id == request.user.id:
                    extra_delete_refusals = True
    return extra_delete_refusals
