from django.shortcuts import render
# pull data from DB
# send email 
    
from django.http import HttpResponse

# Create your views here.
# request handler owo

def say_hi(req):
    x = 1
    y = 2
    return render(req, 'index.html', {'name': 'mamahuevo'})

