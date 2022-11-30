from django.contrib import admin
from . import models

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'country',)


admin.site.register(models.Person)
admin.site.register(models.Role)
