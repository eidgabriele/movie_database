from django.db import models
from django.utils.translation import gettext_lazy as _

class Role(models.Model):
    name = models.CharField(_('name'), max_length=150)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('role')
        verbose_name_plural = _('roles')

class Person(models.Model):
    first_name = models.CharField(_('first name'), max_length=150)
    last_name = models.CharField(_('last name'), max_length=150)
    country = models.CharField(_('country'), max_length=150)
    photo = models.ImageField(_('photo'), upload_to='cast_photos', blank=True, null=True)

    def __str__(self)->str:
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('people')

class Location(models.Model):
    name = models.CharField(_('location name'), max_length=255,)
    country = models.CharField(_('country'), max_length=150)

    def __str__(self) -> str:
        return f"{self.name}, {self.country}"

    class Meta:
        verbose_name = _('location')
        verbose_name_plural = _('locations')


class Genre(models.Model):
    name = models.CharField(_('genre name'), max_length=150)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('genre')
        verbose_name_plural = _('genres')

class Company(models.Model):
    name = models.CharField(_('genre name'), max_length=150)
    country = models.CharField(_('country'), max_length=150)

    def __str__(self) -> str:
        return f"{self.name} ({self.country})"

    class Meta:
        verbose_name = _('company')
        verbose_name_plural = _('companies')


class Language(models.Model):
    name = models.CharField(_('language name'), max_length=150)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _('language')
        verbose_name_plural = _('languages')


class Media(models.Model):
    name = models.CharField(_('movie/series name'), max_length=150)
    release_date = models.DateField(_('release date'), null=True, blank=True)
    score = models.FloatField(_('score'), null=True, blank=True)
    duration = models.IntegerField(_('duration'),)
    is_series = models.BooleanField(_('is series?'), default=False)
    poster = models.ImageField(_('poster'), upload_to='posters', blank=True, null=True)
    trailer = models.CharField(_('trailer link'), max_length=255, blank=True, null=True)
    pg_rating = models.CharField(_('PG rating'), max_length=150, blank=True, null=True)
    summary = models.TextField(_('summary'), blank=True, null=True)
    tagline = models.CharField(_('tagline'), max_length=255, blank=True, null=True )
    budget = models.IntegerField(_('budget'), blank=True, null=True)
    box_office = models.IntegerField(_('box office'), blank=True, null=True)

    location = models.ManyToManyField(Location, verbose_name=_('location'))
    genre = models.ManyToManyField(Genre, verbose_name=_('genre'))
    company = models.ManyToManyField(Company, verbose_name=_('company'))
    language = models.ManyToManyField(Language, verbose_name=_('language'))
    
    def __str__(self) -> str:
        return f"{self.name}, {self.release_date.strftime('%Y')}"

class CastCrew(models.Model):
    role = models.ManyToManyField(Role, verbose_name=_("role"))
    person = models.ManyToManyField(Person, verbose_name=_("person"))
    media = models.ForeignKey(Media, verbose_name=_("media"), on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.person} - {self.role} ({self.media})"

    
class Season(models.Model):
    media = models.ForeignKey(Media, verbose_name=_("media"), on_delete=models.CASCADE)
    

class Episode(models.Model):
    duration = models.IntegerField(_('duration'), default=0)
    release_date = models.DateField(_('release date'), null=True, blank=True)
    season = models.ForeignKey(Season, verbose_name=_('season'), on_delete=models.CASCADE)
