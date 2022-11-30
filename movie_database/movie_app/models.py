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