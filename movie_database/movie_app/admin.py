from django.contrib import admin
from . import models

class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'country',)

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Role, RoleAdmin)
admin.site.register(models.Location)
admin.site.register(models.Genre)
admin.site.register(models.Company)
admin.site.register(models.Language)
admin.site.register(models.Media)
admin.site.register(models.CastCrew)
admin.site.register(models.Season)
admin.site.register(models.Episode)

