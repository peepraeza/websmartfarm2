from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

"""
Category of plants that are created by users
"""
class Vegetable(models.Model):
    type_name = models.CharField(max_length=200)
    duration = models.IntegerField(validators=MinValueValidator(0))
    create_record_timestamp = models.DateTimeField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return self.type_name
        
"""
Vegetables that are being planted in the farm
"""
class Plant(models.Model):
    plant_type = models.CharField(max_length=200)
    sensor = models.CharField(max_length=200)
    start_plant_timestamp = models.DateTimeField()
    end_plant_timestamp = models.DateTimeField()
    create_record_timestamp = models.DateTimeField(default=timezone.now)
    is_harvested = models.BooleanField()
    
    def __str__(self):
        return "{}_{}".format(self._type_name, self._create_record_timestamp)
        
"""
Category of plants that are created by users
"""
class Compost(models.Model):
    plant_id = models.IntegerField()
    compost_type = models.CharField(max_length=30)
    compost_total = models.IntegerField(validators=MinValueValidator(0)) 
    compost_unit = models.CharField(max_length=30)
    compost_date = models.DateTimeField(default=timezone.now)
    create_record_timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.compost_type