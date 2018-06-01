import datetime as dt

from django.shortcuts import render

# Create your views here.


def main(request):
    title = 'this is a test message'
    date = dt.date.today()
    return render(request, 'main/main.html', {"title": title, "date": date})
