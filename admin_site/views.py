from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.template import RequestContext
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.html import strip_tags
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.db.models import Q, Sum
from datetime import date, datetime, timedelta
from django.shortcuts import get_object_or_404
from admin_site.models import *
from admin_site.forms import *
from django.conf import settings


def send_bulk_mail(request):
    if request.method == 'POST':
        email_string = request.POST['emails']
        email_list = email_string.split(",")
        mail_subject = request.POST["subject"]
        email_body = request.POST["body"]
        
        context = {
            'domain': get_current_site(request),
            'subject': mail_subject,
            'body': email_body
            
        }
    
        from_email = settings.EMAIL_HOST_USER
        html_message = render_to_string('site_admin/mail/bulk_mail_template.html', context)
        plain_message = strip_tags(html_message)

        mail_sent = send_mail(mail_subject, plain_message, from_email, email_list, html_message=html_message,
                          fail_silently=True)
        if mail_sent:
            messages.success(request, 'mails sent successfully')
        else:
            messages.error(request, 'error sending mail')
        return redirect('send_mails')

    return render(request, 'site_admin/mail/bulk_mail.html')



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
    context_object_name = "about_info"

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
        return reverse('hero_index')

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


class GalleryCreateView(SuccessMessageMixin, CreateView):
    model = GalleryModel
    form_class = GalleryForm
    template_name = 'site_admin/gallery/create.html'
    success_message = 'Image Added Successfully'

    def get_success_url(self):
        return reverse('gallery_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GalleryListView(ListView):
    model = GalleryModel
    fields = '__all__'
    template_name = 'site_admin/gallery/index.html'
    context_object_name = "gallery_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class GalleryUpdateView(SuccessMessageMixin, UpdateView):
    model = GalleryModel
    form_class = GalleryForm
    template_name = 'site_admin/gallery/edit.html'
    success_message = 'Image Successfully Updated'

    def get_success_url(self):
        return reverse('gallery_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GalleryDeleteView(DeleteView):
    model = GalleryModel
    fields = '__all__'
    template_name = 'site_admin/gallery/delete.html'
    context_object_name = "gallery"

    def get_success_url(self):
        return reverse('gallery_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
