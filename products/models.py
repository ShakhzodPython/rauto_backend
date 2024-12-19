from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

from config.settings import AUTH_USER_MODEL


# Create your models here.

class CarCategory(models.Model):
    title = models.CharField(max_length=70, verbose_name=_('Title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class BodyType(models.Model):
    title = models.CharField(max_length=70, verbose_name=_('Title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    class Meta:
        verbose_name = _('Body type')
        verbose_name_plural = _('Body types')

    def __str__(self):
        return self.title


class Gearbox(models.Model):
    title = models.CharField(max_length=70, verbose_name=_('Title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    class Meta:
        verbose_name = _('Gearbox')
        verbose_name_plural = _('Gearboxes')

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=70, verbose_name=_('Title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    class Meta:
        verbose_name = _('Color')
        verbose_name_plural = _('Colors')

    def __str__(self):
        return self.title


class TypeFuel(models.Model):
    title = models.CharField(max_length=70, verbose_name=_('Title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    class Meta:
        verbose_name = _('Type fuel')
        verbose_name_plural = _('Type fuels')

    def __str__(self):
        return self.title


class MachineCondition(models.Model):
    title = models.CharField(max_length=70, verbose_name=_('Title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    class Meta:
        verbose_name = _('Machine condition')
        verbose_name_plural = _('Machine conditions')

    def __str__(self):
        return self.title


class MachineDrive(models.Model):
    title = models.CharField(max_length=70, verbose_name=_('Title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))

    class Meta:
        verbose_name = _('Machine drive')
        verbose_name_plural = _('Machine drives')

    def __str__(self):
        return self.title


class Car(models.Model):
    class Currency(models.TextChoices):
        SOM = 'som', _('SOM'),
        USD = 'usd', _('USD'),

    class Location(models.TextChoices):
        TASHKENT = 'tashkent', _('Tashkent'),
        SAMARKAND = 'samarkand', _('Samarkand'),

    category = models.ForeignKey(CarCategory,
                                 on_delete=models.CASCADE,
                                 verbose_name=_('category'),
                                 related_name='car')
    title = models.CharField(max_length=70, verbose_name=_('Title'))
    body_type = models.ForeignKey(BodyType,
                                  verbose_name=_('Body type'),
                                  on_delete=models.CASCADE,
                                  related_name='car_body_type')
    images = models.ManyToManyField('media.Media',
                                    verbose_name=_('Images'))
    desc = RichTextField(verbose_name=_('Description'))
    price = models.IntegerField(verbose_name=_('Price'))
    currency = models.CharField(max_length=5, choices=Currency.choices, verbose_name=_('Currency'))
    year = models.IntegerField(verbose_name=_('Year'))
    mileage = models.IntegerField(verbose_name=_('Mileage'))
    gearbox = models.ForeignKey(Gearbox,
                                on_delete=models.CASCADE,
                                verbose_name=_('Gearbox'),
                                related_name='car_gearbox')
    color = models.ForeignKey(Color,
                              on_delete=models.CASCADE,
                              verbose_name=_('Color'),
                              related_name='car_color')
    engine = models.CharField(max_length=5, verbose_name=_('Engine'))
    type_fuel = models.ForeignKey(TypeFuel,
                                  on_delete=models.CASCADE,
                                  verbose_name=_('Type fuel'),
                                  related_name='car_type_fuel')
    machine_condition = models.ForeignKey(MachineCondition,
                                          on_delete=models.CASCADE,
                                          verbose_name=_('Machine condition'),
                                          related_name='car_machine_condition'
                                          )
    machine_drive = models.ForeignKey(MachineDrive,
                                      on_delete=models.CASCADE,
                                      verbose_name=_('Machine drive'),
                                      related_name='car_machine_drive'
                                      )
    location = models.CharField(max_length=50, choices=Location.choices, verbose_name=_('Location'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated at'))
    author = models.ForeignKey(AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               verbose_name=_('Author'),
                               related_name='car_author')

    class Meta:
        verbose_name = _('Car')
        verbose_name_plural = _('Cars')

    def __str__(self):
        return self.title
