# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# import models
from .models import ProfileModel

# Register your models here.
admin.site.register( ProfileModel )

admin.site.site_header = 'Primary School'
admin.site.site_title = "E-learning System administrator "
