from django.contrib import admin
from . import models
admin.site.register(models.Host)
admin.site.register(models.HostDetails)

# Register your models here.
