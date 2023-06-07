from typing import Set
from django.db import models
from django.urls import reverse_lazy


# Create your models here.


class Oblast(models.Model):
    name = models.CharField(
        verbose_name="Oblast name",
        max_length=20
    )
    description = models.TextField(
        verbose_name="Region description",
        null=True,
        blank=True,
    )
    def __str__(self):
        return self.name

class Region(models.Model):
    oblast = models.ForeignKey(
        "spravochniki.Oblast",
        on_delete=models.PROTECT,
        verbose_name="Oblast",
        default=1,
        related_name="regions"
    )
    name = models.CharField(
        verbose_name="Region name",
        max_length=20
    )
    description = models.TextField(
        verbose_name="Region description",
        null=True,
        blank=True,
    )
    def __str__(self):
        return self.name

class City(models.Model):
    region = models.ForeignKey(
        "spravochniki.Region",
        on_delete=models.PROTECT,
        verbose_name="Region",
        related_name="cities"
    )
    name = models.CharField(
        verbose_name="City name",
        max_length=20
    )
    description = models.TextField(
        verbose_name="City description",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
        
    
    def get_absolute_url(self):
        return reverse_lazy('spravochniki:view-city', kwargs={"pk": self.pk})
        return f"/city-cbv/{self.pk}"
    
class PublicHolidays(models.Model):
    name = models.CharField(
        verbose_name="Holiday name",
        max_length=255
    )
    holiday_date = models.DateField(
        verbose_name="holiday date"
    )
    description = models.TextField(
        verbose_name="Holiday description",
        null=True,
        blank=True,
    )
    created = models.DateField(
        verbose_name="created datetime",
        auto_now=False,
        auto_now_add=True 

    )
    updated = models.DateField(
        verbose_name="updated datetime",
        auto_now=True,
        auto_now_add=False
    )
    def __str__(self):
        return self.name