def get_request_metadata(request):
    meta_dict = dict()
    if 'REMOTE_ADDR' in request.META:
        meta_dict['REMOTE_ADDR'] = request.META['REMOTE_ADDR']
    if 'REMOTE_HOST' in request.META:
        meta_dict['REMOTE_ADDR'] = request.META['REMOTE_HOST']
    if 'REMOTE_USER' in request.META:
        meta_dict['REMOTE_ADDR'] = request.META['REMOTE_USER']
    if 'HTTP_USER_AGENT' in request.META:
        meta_dict['REMOTE_ADDR'] = request.META['HTTP_USER_AGENT']
    return meta_dict
