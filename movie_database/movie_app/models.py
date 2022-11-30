from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Role(models.Model):
    name = models.CharField(_('name'), max_length=150, help_text=_('Enter the name of the role'))

    def __str__(self)->str:
        return self.name

class Person(models.Model):
    first_name = models.CharField(_('first name'), max_length=100)
    last_name = models.CharField(_('last name'), max_length=100)
    country = models.CharField(_('country'), max_length=100)
    photo = models.ImageField(_('photo'), upload_to='cast_photos', blank=True, null=True)

    def __str__(self)->str:
        return f"{self.first_name} {self.last_name}"