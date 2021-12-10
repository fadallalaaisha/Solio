
from django.shortcuts import render
from django.http import HttpResponse
# from calendar import HTMLCalendar
 
def index(request,year,month):
    name='Aisha'
    year='year'
    month='month'
    return render(request,"calendar.html",{"name":name})

