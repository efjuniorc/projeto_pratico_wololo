from _mysql import IntegrityError
from datetime import datetime, timedelta

import django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, AccessMixin
from django.contrib.auth.models import User
from django.db.models import Sum
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, RedirectView, ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin

from core.forms import LinkForm
from core.messeges_utils import message_error_generic, message_sucess_generic, message_info_generic
from core.models import Link


class TestaEmpresaMixin(SingleObjectMixin, AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        try:
            if self.get_object().empresa == request.user.user_profile.empresa:
                return super().dispatch(request, *args, **kwargs)
            else:
                return HttpResponse(status=500)
        except Exception as e:
            print('exceção no TESTE EMPRESA MIXIN', e)
            return super().dispatch(request, *args, **kwargs)


class LoginView(TemplateView):
    template_name = 'core/paginas/login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return self.redirect_after_login(user)

        message = 'Usuário ou senha incorretos!!'
        message_error_generic(request, message)
        return self.render_to_response({'message': message})

    def redirect_after_login(self, user):
        print('redirect_after_login')
        if user.is_superuser:
            return redirect('/admin/')
        return redirect('core:index')


class LogoutRedirectViews(RedirectView):
    url = '/login/'

    @method_decorator(login_required(login_url='/login'))
    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class Dashboard(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['links_cadastrados'] = Link.objects.all()
        return context

    def get_success_url(self):
        return reverse('core:index')


class RedirectLink(RedirectView):
    def get(self, request, *args, **kwargs):
        link = Link.objects.get(url_encurtado=kwargs['url'])
        link.contador += 1
        link.save()
        return redirect(link.url_original)


class LinkCreateView(CreateView):
    model = Link
    template_name = 'core/link/link_create_update_view.html'
    success_url = reverse_lazy("core:index")
    form_class = LinkForm

class LinkUpdateView(UpdateView):
    model = Link
    template_name = 'core/link/link_create_update_view.html'
    success_url = reverse_lazy("core:index")
    form_class = LinkForm


class LinkDeleteView(DeleteView):
    model = Link
    template_name = 'core/base/delete_view_generic.html'
    success_url = reverse_lazy("core:index")

    def delete(self, request, *args, **kwargs):
        message_info_generic(self.request, "Registro Deletado Com Sucesso")
        return super(LinkDeleteView, self).delete(request, *args, **kwargs)
