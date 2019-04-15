from __future__ import unicode_literals

from django.contrib import admin

# import models
from .models import PdfResources,EResources

# Register your models here.
admin.site.register( EResources )

admin.site.site_header = 'Primary School'
admin.site.site_title = "E-learning System administrator "
