from pydoc import locate

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

from core.form.form import FormBuilder
from core.form.formset import FormsetBuilder
from core.form.passwordform import PasswordformBuilder
from core.globals.global_base import PrivateBase
from core.globals.global_ctx import create_chapterctxdata
from core.globals.global_functions import set_ajax_variables, is_ajax_request, decode_string, prepare_message, update_successurl
from crispy_forms.utils import render_crispy_form
from django.db.models import ProtectedError
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.template.context_processors import csrf
from django.template.loader import render_to_string
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from shared.variables.view_variables import set_user_variables


class GlobalTemplate(PrivateBase, TemplateView):
    viewtype = "template"

    def get_context_data(self, **kwargs):

        # Prevent server from repeating downloads when 'print_records' still is in data
        if 'print_records' in self.data:
            del self.data['print_records']
            del self.data['print_type']

        if 'variables_loaded' not in self.request.session:
            set_user_variables(self.request)
        context = super().get_context_data(**kwargs)
        self.ctx = create_chapterctxdata(self.request, self.viewtype)
        context.update({"ctx": self.ctx})
        return context

    def render_to_response(self, context, **response_kwargs):  # Check if the request is Ajax or not
        if not self.ctx['rights']['read']:
            return HttpResponseNotAllowed("Geen rechten")
        return super(GlobalTemplate, self).render_to_response(context, **response_kwargs)


class GlobalCreate(PrivateBase, CreateView):
    viewtype = "create"
    templatename = None

    def get_context_data(self, **kwargs):
        self.data = dict()
        context = super().get_context_data(**kwargs)
        context.update({"ctx": self.ctx})
        return context

    def get_form(self, form=None, **kwargs):
        self.ctx = create_chapterctxdata(self.request, self.viewtype)
        if self.request.GET.get('formset', '') == 'true':
            form = FormsetBuilder(self.request, self.ctx).create()
        else:
            form = FormBuilder(self.request, self.ctx).create()
        return form

    def render_to_response(self, context, **response_kwargs):  # Check if the request is Ajax or not
        if is_ajax_request(self.request):
            if not self.ctx['rights']['write']:
                data = dict()
                data['not_allowed'] = True
            else:
                set_ajax_variables(self.request, self.ctx, self.data, context, self.templatename)
                data = self.data
            self.data = dict()
            return JsonResponse(data, safe=False, **response_kwargs)
        else:
            if not self.ctx['rights']['write']:
                return HttpResponseNotAllowed("Geen rechten")
            self.templatename = self.ctx['templatename']
            return super(GlobalCreate, self).render_to_response(context, **response_kwargs)

    def form_invalid(self, form):  # Do stuff with the content before saving the form
        print("Form errors:", form.errors)
        if self.request.GET.get('level') == '0':
            context = {'form': form}
            htmlform = render_to_string(self.templatename, context, request=self.request)
            return HttpResponse(htmlform)
        else:
            context = {'ctx': self.ctx}
            context.update(csrf(self.request))
            self.data['html_body'] = render_crispy_form(form, context=context)
            self.data['form_is_valid'] = False
            data = self.data
            self.data = dict()
            return JsonResponse(data)

    def form_valid(self, form, **kwargs):  # Do stuff with the content before saving the form
        if not self.ctx['rights']['write']:
            data = dict()
            data['not_allowed'] = True
        else:
            successurl = self.request.GET.get('successurl', '')
            self.data['successurl'] = decode_string(successurl)
            if self.request.GET.get('formset', '') == 'true':
                form.save()
            else:
                record = form.save()
                self.data['successurl'] = update_successurl(self.data['successurl'], record.id)
                add_extra_execute_options = getattr(locate('shared.extra_execute_options'), 'add_extra_execute_options')
                if add_extra_execute_options and self.ctx['package']:  # Check the existance of the file extra_refusals.py in shared
                    add_extra_execute_options(self, record)
            self.data['level'] = self.request.GET.get('level', '')
            prepare_message(self.request, self.ctx, self.data, messages)
            self.data['form_is_valid'] = True
            data = self.data
            self.data = dict()
        return JsonResponse(data, status=200)


class GlobalUpdate(PrivateBase, UpdateView):
    viewtype = "update"
    templatename = None

    def get_object(self, **kwargs):
        record = super().get_jsondata_update(self.request, self.kwargs)
        self.context_object_name = "record"
        self.ctx = create_chapterctxdata(self.request, self.viewtype, self.kwargs['pk'])
        return record

    def get_form(self, form=None, **kwargs):
        if self.request.GET.get('passwordform', '') == 'true':
            form = PasswordformBuilder(self.request, self.ctx).update()
        else:
            form = FormBuilder(self.request, self.ctx).update()
        return form

    def get_context_data(self, **kwargs):
        self.data = dict()
        context = super().get_context_data(**kwargs)
        context.update({'ctx': self.ctx})
        return context

    def render_to_response(self, context, **response_kwargs):  # Check if the request is Ajax or not
        if is_ajax_request(self.request):
            if not self.ctx['rights']['write']:
                data = dict()
                data['not_allowed'] = True
            else:
                set_ajax_variables(self.request, self.ctx, self.data, context, self.templatename)
                data = self.data
            self.data = dict()
            return JsonResponse(data, safe=False, **response_kwargs)
        else:
            if not self.ctx['rights']['write']:
                return HttpResponseNotAllowed("Geen rechten")
            self.templatename = self.ctx['templatename']
            return super(GlobalUpdate, self).render_to_response(context, **response_kwargs)

    def form_invalid(self, form):  # Do stuff with the content before saving the form
        print("Form errors:", form.errors)
        if self.request.GET.get('level') == '0':
            context = {'form': form}
            htmlform = render_to_string(self.templatename, context, request=self.request)
            return HttpResponse(htmlform)
        else:
            context = {'ctx': self.ctx}
            context.update(csrf(self.request))
            self.data['html_body'] = render_crispy_form(form, context=context)
            self.data['form_is_valid'] = False
            data = self.data
            self.data = dict()
            return JsonResponse(data)

    def form_valid(self, form, **kwargs):  # Do stuff with the content before saving the form
        if not self.ctx['rights']['write']:
            data = dict()
            data['not_allowed'] = True
        else:
            record = form.save()
            if self.request.GET.get('passwordform', '') == 'true':
                update_session_auth_hash(self.request, form.user)
            if 'status_current' in self.ctx and 'status_next' in self.ctx:
                if record.status == self.ctx['status_current']:
                    record.status = self.ctx['status_next']
                    record.save()
            successurl = self.request.GET.get('successurl', '')
            self.data['successurl'] = decode_string(successurl)
            self.data['successurl'] = update_successurl(self.data['successurl'], record.id)
            self.data['level'] = self.request.GET.get('level', '')

            # Check extra update_actions to add to self.data
            if 'print_records' in self.data:
                del self.data['print_records']
            if 'print_type' in self.data:
                del self.data['print_type']
            add_extra_execute_options = getattr(locate('shared.extra_execute_options'), 'add_extra_execute_options')
            if add_extra_execute_options and self.ctx['package']:  # Check the existance of the file extra_refusals.py in shared
                add_extra_execute_options(self, record)

            prepare_message(self.request, self.ctx, self.data, messages)
            self.data['form_is_valid'] = True
            data = self.data
            self.data = dict()
        return JsonResponse(data)


class GlobalDelete(PrivateBase, DeleteView):
    viewtype = "delete"
    templatename = None

    def get_object(self, **kwargs):
        record = super().get_jsondata_delete(self.request, self.kwargs)
        self.context_object_name = "record"
        self.ctx = create_chapterctxdata(self.request, self.viewtype, self.kwargs['pk'])
        return record

    def get_form(self, form=None, **kwargs):
        form = FormBuilder(self.request, self.ctx).delete()
        return form

    def get_context_data(self, **kwargs):
        self.data = dict()
        context = super().get_context_data(**kwargs)
        self.ctx['footer_button_html'] = "core/actions/delete.html"
        context.update({'ctx': self.ctx})
        return context

    def render_to_response(self, context, **response_kwargs):  # Delete is always Ajax
        if is_ajax_request(self.request):
            if not self.ctx['rights']['write']:
                data = dict()
                data['not_allowed'] = True
            else:
                set_ajax_variables(self.request, self.ctx, self.data, context, self.templatename)
                data = self.data
            self.data = dict()
            return JsonResponse(data, safe=False, **response_kwargs)
        else:
            if not self.ctx['rights']['write']:
                return HttpResponseNotAllowed("Geen rechten")
            self.templatename = self.ctx['templatename']
            return super(GlobalDelete, self).render_to_response(context, **response_kwargs)

    def form_invalid(self, form):  # Do stuff with the content before saving the form
        print("Form errors:", form.errors)
        if self.request.GET.get('level') == '0':
            context = {'form': form}
            htmlform = render_to_string(self.templatename, context, request=self.request)
            return HttpResponse(htmlform)
        else:
            context = {'ctx': self.ctx}
            context.update(csrf(self.request))
            self.data['html_body'] = render_crispy_form(form, context=context)
            self.data['form_is_valid'] = False
            data = self.data
            self.data = dict()
            return JsonResponse(data)

    def form_valid(self, request, *args, **kwargs):
        if not self.ctx['rights']['write']:
            data = dict()
            data['not_allowed'] = True
        else:
            closelevel = None
            if self.request.GET.get('closelevel', ''):
                closelevel = int(self.request.GET.get('closelevel'))

            try:
                # Check extra refusals before delete
                extra_delete_refusals = False
                check_extra_delete_refusals = getattr(locate('shared.extra_refusals'), 'check_extra_delete_refusals')
                if check_extra_delete_refusals and self.ctx['package'] and self.ctx['modelname']:  # Check the existance of the file extra_refusals.py in shared
                    extra_delete_refusals = check_extra_delete_refusals(self.request, self.ctx['package'], self.ctx['modelname'], self.object)

                if not self.ctx['deny_del_or_upd'] and not extra_delete_refusals:
                    self.object.delete()
                self.data['form_is_valid'] = True
            except ProtectedError:
                self.data['form_is_valid'] = False
            self.data['successurl'] = decode_string(self.request.GET.get('successurl'))
            self.data['level'] = self.ctx['level']
            prepare_message(request, self.ctx, self.data, messages)
            if closelevel:
                self.data['closelevel'] = closelevel  # This, to also close the update_modal via ajax.js
            data = self.data
            self.data = dict()
        return JsonResponse(data)
