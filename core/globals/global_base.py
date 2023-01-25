from core.globals.global_functions import check_session_variables
from core.globals.global_record_delete import delete_record
from core.globals.global_record_update import update_record


class PrivateBase:
    context_object_name = None
    template_name = "core/content/content.html"
    templatename = None
    ctx = None
    data = dict()

    def get_jsondata_update(self, request, kwargs):
        check_session_variables(request)
        """ Get the record"""
        record = update_record(request, kwargs['pk'])
        self.context_object_name = 'record'
        return record

    def get_jsondata_delete(self, request, kwargs):
        check_session_variables(request)
        """ Get the record"""
        record = delete_record(request, kwargs['pk'])
        self.context_object_name = 'record'
        return record


class PublicBase:
    context_object_name = None
    template_name = "core/content/public.html"
    templatename = None
    ctx = None
    data = dict()

    def get_jsondata_update(self, request, kwargs):
        check_session_variables(request)
        """ Get the record"""
        record = update_record(request, kwargs['pk'])
        self.context_object_name = 'record'
        return record

    def get_jsondata_delete(self, request, kwargs):
        check_session_variables(request)
        """ Get the record"""
        record = delete_record(request, kwargs['pk'])
        self.context_object_name = 'record'
        return record
