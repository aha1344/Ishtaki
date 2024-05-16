from django.db import models
from .choices import corruption_types, sector_types, cities
# Create your models here.
class Report(models.Model):
    corruption_type = models.CharField(max_length = 100, choices = corruption_types)
    public_sector_type = models.CharField(max_length = 500, choices = sector_types, default = "")
    public_sector_name = models.CharField(max_length = 500, default = "")
    date_of_incident = models.DateTimeField()
    city = models.CharField(max_length=100, choices = cities, default = "بيروت")
    street = models.CharField(max_length=100, default = "")


