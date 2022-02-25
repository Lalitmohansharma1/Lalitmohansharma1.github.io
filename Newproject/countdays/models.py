from django.db import models
import datetime
from datetime import date
# Create your models here.
class initialdate(models.Model):
    day=models.CharField(max_length=2)
    month=models.CharField(max_length=2)
    year=models.CharField(max_length=4)
    finalday=models.CharField(max_length=2)
    finalmonth=models.CharField(max_length=2)
    finalyear=models.CharField(max_length=4)

    def __str__(self):
        # return f"{ self.finalday}-{self.finalmonth}-{self.finalyear} to {self.day}-{self.month}-{self.year}"
        self.d0=date(int(self.finalyear),int(self.finalmonth),int(self.finalday))
        self.d1=date(int(self.year),int(self.month),int(self.day))
        self.Ndays=str((self.d0-self.d1).days)
        return self.Ndays