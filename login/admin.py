from django.contrib import admin
from . import models
from django.contrib.admin import AdminSite
from django.utils import translation

# Register your models here.
admin.site.register(models.User)

class MyAdminSite(AdminSite):
    site_title = translation.gettext_lazy('跌倒检测系统')
    site_header = translation.gettext_lazy("管理员登录")


admin_site = MyAdminSite()
admin_site.register(models.User)








