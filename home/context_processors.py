from admin_site.models import *


def layout_variable(request):
    site_info = SiteInfoModel.objects.first()
    about_info = SiteAboutInfoModel.objects.first()

    return {
        'site_info': site_info,
        'about_info': about_info,

        }



