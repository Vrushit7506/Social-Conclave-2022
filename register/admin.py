from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Delegate)

@admin.register(Delegate)
class DelegateAdmin(ImportExportModelAdmin):
    pass