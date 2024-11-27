from django.urls import path
from home.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('contact-us', ContactPageView.as_view(), name='contact'),
    path('donate', DonatePageView.as_view(), name='donate'),
    path('event', EventPageView.as_view(), name='event'),

]

