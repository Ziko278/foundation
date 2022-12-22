from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Q, Sum
from datetime import date, datetime, timedelta
from django.shortcuts import get_object_or_404
from admin_site.models import *
from admin_site.forms import *


class AdminDashboardView(TemplateView):
    template_name = 'site_admin/dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context


class SiteInfoCreateView(SuccessMessageMixin, CreateView):
    model = SiteInfoModel
    form_class = SiteInfoForm
    template_name = 'site_admin/info/create.html'
    success_message = 'Site Info Saved successfully'

    def dispatch(self, *args, **kwargs):
        try:
            site_info = SiteInfoModel.objects.get(pk=1)
        except SiteInfoModel.DoesNotExist:
            return super(SiteInfoCreateView, self).dispatch(*args, **kwargs)
        return redirect(reverse('admin_dashboard'))

    def get_success_url(self):
        return reverse('site_info_detail', kwargs={'pk':self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SiteInfoUpdateView(SuccessMessageMixin, UpdateView):
    model = SiteInfoModel
    form_class = SiteInfoForm
    template_name = 'site_admin/info/update.html'
    success_message = 'Organization Info Saved successfully'

    def get_success_url(self):
        return reverse('site_info_detail', kwargs={'pk':self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        
        

class SiteInfoDetailView(SuccessMessageMixin, DetailView):
    model = SiteInfoModel
    template_name = 'site_admin/info/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        
        
class SiteAboutInfoCreateView(SuccessMessageMixin, CreateView):
    model = SiteAboutInfoModel
    form_class = SiteAboutInfoForm
    template_name = 'site_admin/about/create.html'
    success_message = 'Site Info Saved successfully'

    def dispatch(self, *args, **kwargs):
        try:
            site_info = SiteAboutInfoModel.objects.get(pk=1)
        except SiteAboutInfoModel.DoesNotExist:
            return super(SiteAboutInfoCreateView, self).dispatch(*args, **kwargs)
        return redirect(reverse('admin_dashboard'))

    def get_success_url(self):
        return reverse('site_about_info_detail', kwargs={'pk':self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SiteAboutInfoUpdateView(SuccessMessageMixin, UpdateView):
    model = SiteAboutInfoModel
    form_class = SiteAboutInfoForm
    template_name = 'site_admin/about/update.html'
    success_message = 'Organization About Info Saved successfully'

    def get_success_url(self):
        return reverse('site_about_info_detail', kwargs={'pk':self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        
        

class SiteAboutInfoDetailView(SuccessMessageMixin, DetailView):
    model = SiteAboutInfoModel
    template_name = 'site_admin/about/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class SiteHeroCreateView(SuccessMessageMixin, CreateView):
    model = SiteHeroModel
    form_class = SiteHeroForm
    template_name = 'site_admin/hero/create.html'
    success_message = 'Banner Added Successfully'

    def get_success_url(self):
        return reverse('hero_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SiteHeroListView(ListView):
    model = SiteHeroModel
    fields = '__all__'
    template_name = 'site_admin/hero/index.html'
    context_object_name = "banner_list"

    def get_queryset(self):
        return SiteHeroModel.objects.all().order_by('order')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SiteHeroDetailView(DetailView):
    model = SiteHeroModel
    fields = '__all__'
    template_name = 'site_admin/hero/detail.html'
    context_object_name = "banner"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SiteHeroUpdateView(SuccessMessageMixin, UpdateView):
    model = SiteHeroModel
    form_class = SiteHeroForm
    template_name = 'site_admin/hero/edit.html'
    success_message = 'Banner Successfully Updated'

    def get_success_url(self):
        return reverse('hero_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SiteHeroDeleteView(DeleteView):
    model = SiteHeroModel
    fields = '__all__'
    template_name = 'site_admin/hero/delete.html'
    context_object_name = "banner"

    def get_success_url(self):
        return reverse('hero_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        
        
class CauseCreateView(SuccessMessageMixin, CreateView):
    model = CauseModel
    form_class = CauseForm
    template_name = 'site_admin/cause/create.html'
    success_message = 'Cause Added Successfully'

    def get_success_url(self):
        return reverse('cause_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CauseListView(ListView):
    model = CauseModel
    fields = '__all__'
    template_name = 'site_admin/cause/index.html'
    context_object_name = "cause_list"

    def get_queryset(self):
        return CauseModel.objects.filter(status='active')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CauseDetailView(DetailView):
    model = SiteHeroModel
    fields = '__all__'
    template_name = 'site_admin/cause/detail.html'
    context_object_name = "cause"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CauseUpdateView(SuccessMessageMixin, UpdateView):
    model = CauseModel
    form_class = CauseForm
    template_name = 'site_admin/cause/edit.html'
    success_message = 'Cause Successfully Updated'

    def get_success_url(self):
        return reverse('cause_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CauseDeleteView(DeleteView):
    model = CauseModel
    fields = '__all__'
    template_name = 'site_admin/cause/delete.html'
    context_object_name = "cause"

    def get_success_url(self):
        return reverse('cause_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
