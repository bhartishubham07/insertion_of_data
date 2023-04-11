from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def insert_Topic(request):
    Tn = input('Enter Topic Name : ')
    TO = Topic.objects.get_or_create(topic_name = Tn)[0]
    TO.save()
    return HttpResponse('<center><h1>Topic Data Inserted Successfully</h1></center')


def insert_Webpage(request):
    Tn = input('Enter Topic Name : ')
    N = input('Enter Name : ')
    url = input('Enter URL : ')
    TO = Topic.objects.get_or_create(topic_name = Tn)[0]
    TO.save()
    WO = Webpage.objects.get_or_create(topic_name=TO, name=N, url=url)[0]
    WO.save()
    return HttpResponse('<center><h1>Webpage Data Inserted Successfully</h1></center')


def insert_AccessRecords(request):
    Tn = input('Enter Topic Name : ')
    N = input('Enter Name : ')
    url = input('Enter URL : ')
    A = input('Enter Author : ')
    D = input('Enter Date : ')
    TO = Topic.objects.get_or_create(topic_name = Tn)[0]
    TO.save()
    WO = Webpage.objects.get_or_create(topic_name=TO, name=N, url=url)[0]
    WO.save()
    AR= AccessRecords.objects.get_or_create(name=WO, author=A, date=D)[0]
    AR.save()
    return HttpResponse('<center><h1>AccessRecords Data Inserted Successfully</h1></center')