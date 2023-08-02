from django.db import models

# Create your models here.
class CLAP(models.Model):
    full_name=models.CharField(max_length=100)
    address=models.CharField(max_length=50)
    neighborhood=models.CharField(max_length=15)
    birth_date_day=models.CharField(max_length=10)
    birth_date_month=models.CharField(max_length=10)
    birth_date_year=models.CharField(max_length=10)
    age=models.CharField(max_length=10)
    ethnicity=models.CharField(max_length=20)


    def __str__(self):
        return self.full_name
