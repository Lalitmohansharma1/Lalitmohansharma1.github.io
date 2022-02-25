from django.shortcuts import render
from .models import initialdate
import datetime
from datetime import date

# Create your views here.
def index(request):
    

    # daa=(date(int(df.finalyear),int(df.finalmonth),int(df.finalday))-date(int(da.year),int(da.month),int(da.day))).days
    return render(request,"countdays/index.html",{
        "days":initialdate.objects.all()
    })