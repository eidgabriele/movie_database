from django.contrib import admin
from . import models


class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'country',)


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CastCrewAdmin(admin.ModelAdmin):
    list_display= ('person', 'role', 'media',)


class CastCrewInLine(admin.TabularInline):
    model = models.CastCrew
    extra = 0
    can_delete= True


class MediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'release_date', 'duration', 'is_series',)
    inlines = (CastCrewInLine, )


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'country',)
    inlines = (CastCrewInLine, )


class EpisodeInLine(admin.TabularInline):
    model = models.Episode
    extra = 0
    can_delete= True


class SeasonAdmin(admin.ModelAdmin):
    list_display = ('number', 'media',)
    inlines = (EpisodeInLine, )


class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'season', )


admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Role, RoleAdmin)
admin.site.register(models.Location, LocationAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.Language, LanguageAdmin)
admin.site.register(models.Media, MediaAdmin)
admin.site.register(models.CastCrew, CastCrewAdmin)
admin.site.register(models.Season, SeasonAdmin)
admin.site.register(models.Episode, EpisodeAdmin)
admin.site.register(models.Watchlist)

