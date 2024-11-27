from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.core.exceptions import PermissionDenied
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.template import RequestContext
from django.http import HttpResponse
from django.urls import reverse
import random
from django.contrib.auth.models import User
from admin_site.models import *


class HomePageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner_list'] = SiteHeroModel.objects.filter(status='active')
        context['cause_list'] = CauseModel.objects.filter(status='active').order_by('order')
        context['gallery_list'] = GalleryModel.objects.all()[:6]
        
        return context
        
        
class AboutPageView(TemplateView):
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
        
        
class ContactPageView(TemplateView):
    template_name = 'home/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
        
        
class DonatePageView(TemplateView):
    template_name = 'home/donate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context



class ConstructionPageView(TemplateView):
    template_name = 'home/construction.html'



class EventPageView(TemplateView):
    template_name = 'home/event.html'

