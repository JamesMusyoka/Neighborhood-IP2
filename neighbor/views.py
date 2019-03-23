from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import *

def home(request):
    date = dt.date.today()
    return render(request, 'home.html', {"date": date})


def neighborhood(request):
    date = dt.date.today()
    return render(request, 'neighborhood.html', {"date": date})

def convert_dates(dates):

    
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    day = days[day_number]
    return day

def past_days_neighborhood(request,past_date):
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
        day = convert_dates(date)
        html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''

        try:
            date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

        except ValueError:
            raise Http404()
            assert False

        if date == dt.date.today():
            return redirect('neighbor')

        return render(request, 'hoods/past_days_neighborhood.html', {"date": date})