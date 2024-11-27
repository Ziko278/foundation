from django.db import models
from django.db.models import Sum


# Create your models here.
class SiteInfoModel(models.Model):
    name = models.CharField(max_length=100)
    logo = models.FileField(upload_to='images/logo', null=True, blank=True)
    mobile_1 = models.CharField(max_length=20, null=True, blank=True)
    mobile_2 = models.CharField(max_length=20, null=True, blank=True)
    info_email = models.EmailField(max_length=100, null=True, blank=True)
    support_email = models.EmailField(max_length=100, null=True, blank=True)
    whatsapp = models.CharField(max_length=100, null=True, blank=True)
    facebook_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    youtube_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)


class SiteHeroModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to='images/hero')
    STATUS = (('active', 'ACTIVE'), ('inactive', 'INACTIVE'))
    status = models.CharField(max_length=20, choices=STATUS)
    URL = (('about', 'ABOUT'), ('donate', 'DONATE'))
    url = models.CharField(max_length=50, choices=URL, blank=True, null=True)
    button_text = models.CharField(max_length=50, null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title.upper()


class SiteAboutInfoModel(models.Model):
    title = models.CharField(max_length=100)
    intro_description = models.TextField()
    main_description = models.TextField()
    founder_name = models.CharField(max_length=100)
    main_image = models.FileField(upload_to='images/about')
    other_image = models.FileField(upload_to='images/about')
    
    
    
class CauseModel(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.FileField(upload_to='images/hero')
    STATUS = (('active', 'ACTIVE'), ('inactive', 'INACTIVE'))
    status = models.CharField(max_length=20, choices=STATUS)
    goal = models.FloatField()
    raised = models.FloatField(default=0)
    order = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title.upper()
        
    def progress(self):
        if self.raised/self.goal > 1:
            return 100
        return round((self.raised/self.goal)*100)


class GalleryModel(models.Model):
    title = models.CharField(max_length=250)
    image = models.FileField(upload_to='images/gallery')


    def __str__(self):
        return self.title.upper()

