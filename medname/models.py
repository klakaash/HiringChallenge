from django.db import models

# Create your models here.

class MedicineName(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    price = models.FloatField(null=True, default=0.0)
    manufacturer = models.CharField(max_length=255, null=True, blank=True)
    salt_name = models.CharField(max_length=255, null=True, blank=True)
    drug_form = models.CharField(max_length=255, null=True, blank=True)
    pack_size = models.CharField(max_length=255, null=True, blank=True)
    strength = models.CharField(max_length=255, null=True, blank=True)
