from django.db import models
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe

# Create your models here.
class Paitent(models.Model):
    name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    Female = 'Female'
    Male = 'Male'
    PossibleGender = ( (Male,'Male'),(Female,'Female') )
    gender = models.CharField(
        max_length=10,
        choices = PossibleGender,
        default= Female,
    )
    age = models.PositiveSmallIntegerField()
    symptoms = models.TextField()
    past_history = models.TextField()
                                        