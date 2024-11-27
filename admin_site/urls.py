from django.urls import path
from admin_site.views import *


urlpatterns = [
    path('', AdminDashboardView.as_view(), name='admin_dashboard'),

    path('mails/send', send_bulk_mail, name='send_mails'),
    
    path('info/create', SiteInfoCreateView.as_view(), name='site_info_create'),
    path('info/detail/<int:pk>', SiteInfoDetailView.as_view(), name='site_info_detail'),
    path('info/update/<int:pk>', SiteInfoUpdateView.as_view(), name='site_info_update'),
    
    
    path('about/create', SiteAboutInfoCreateView.as_view(), name='site_about_info_create'),
    path('about/detail/<int:pk>', SiteAboutInfoDetailView.as_view(), name='site_about_info_detail'),
    path('about/update/<int:pk>', SiteAboutInfoUpdateView.as_view(), name='site_about_info_update'),
    
    
    path('hero/add', SiteHeroCreateView.as_view(), name='hero_create'),
    path('hero/index', SiteHeroListView.as_view(), name='hero_index'),
    path('hero/<int:pk>/detail', SiteHeroDetailView.as_view(), name='hero_detail'),
    path('hero/<int:pk>/edit', SiteHeroUpdateView.as_view(), name='hero_edit'),
    path('hero/<int:pk>/delete', SiteHeroDeleteView.as_view(), name='hero_delete'),
    
    
    path('cause/add', CauseCreateView.as_view(), name='cause_create'),
    path('cause/index', CauseListView.as_view(), name='cause_index'),
    path('cause/<int:pk>/detail', CauseDetailView.as_view(), name='cause_detail'),
    path('cause/<int:pk>/edit', CauseUpdateView.as_view(), name='cause_edit'),
    path('cause/<int:pk>/delete', CauseDeleteView.as_view(), name='cause_delete'),
   

    path('gallery/add', GalleryCreateView.as_view(), name='gallery_create'),
    path('gallery/index', GalleryListView.as_view(), name='gallery_index'),
    path('gallery/<int:pk>/edit', GalleryUpdateView.as_view(), name='gallery_edit'),
    path('gallery/<int:pk>/delete', GalleryDeleteView.as_view(), name='gallery_delete'),

    
]

