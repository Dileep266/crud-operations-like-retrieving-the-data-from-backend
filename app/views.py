from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.

def display_topic(request):
    QLTO=Topic.objects.all()
    d={'QLTO':QLTO}
    return render(request,'display_topic.html',context=d)

def display_web(request):
     WLTO=Webpage.objects.all()
     WLTO=Webpage.objects.all().order_by()
     WLTO=Webpage.objects.all().order_by('topic_name')
     WLTO=Webpage.objects.all().order_by('-topic_name')
     WLTO=Webpage.objects.all().order_by(Length('topic_name'))
     WLTO=Webpage.objects.all().order_by(-Length('topic_name'))
     WLTO=Webpage.objects.all().order_by(Length('topic_name').desc())
     WLTO=Webpage.objects.filter().exclude(topic_name='Football')
     WLTO=Webpage.objects.filter(name='msd')
     WLTO=Webpage.objects.filter(name__gt='msd')
     WLTO=Webpage.objects.filter(name__gte='msd')
     WLTO=Webpage.objects.filter(pk__lt=5)
     WLTO=Webpage.objects.filter(name__lt='msd')
     WLTO=Webpage.objects.filter(name__lte='msd')
     WLTO=Webpage.objects.filter(name__gt='msd')
     WLTO=Webpage.objects.filter(name__lt='msd')
     WLTO=Webpage.objects.filter(name__lte='msd')
     WLTO=Webpage.objects.filter(name='msd')
     WLTO=Webpage.objects.filter(name__contains='m')
     WLTO=Webpage.objects.filter(name__startswith='r')
     WLTO=Webpage.objects.filter(name__endswith='d')
     WLTO=Webpage.objects.all()
     WLTO=Webpage.objects.filter(topic_name__in=('cricket','Football'))
     WLTO=Webpage.objects.all()
     WLTO=Webpage.objects.filter(topic_name='cricket',name='msd')
     WLTO=Webpage.objects.filter(Q(topic_name='cricket')|Q(topic_name='Football'))
     WLTO=Webpage.objects.filter(topic_name='cricket',email__startswith='india')
     WLTO=Webpage.objects.filter(Q(email__startswith='india')& Q(url__endswith='virat'))
     WLTO=Webpage.objects.filter(Q(email__startswith='india')| Q(url__endswith='virat'))
     WLTO=Webpage.objects.filter(Q(email__startswith='india')& Q(url__endswith='virat'))
     WLTO=Webpage.objects.filter(name='ronaldo',topic_name='cricket')
     WLTO=Webpage.objects.filter(Q(name='ronaldo')|Q(topic_name='cricket')|Q(name__contains='msd'))
     WLTO=Webpage.objects.filter(name__contains='msd')
     WLTO=Webpage.objects.filter(email__contains='chetri')
     WLTO=Webpage.objects.filter(name='ronaldo')


     
     
     
     d={'WLTO':WLTO}
     return render(request,'display_webpage.html',d)
     
def display_accessrecord(request):
     ALTO=Accessrecord.objects.all()
     ALTO=Accessrecord.objects.filter(date__year=2022)
     ALTO=Accessrecord.objects.filter(date__year__gte=2022)
     ALTO=Accessrecord.objects.filter(date__month=12)
     ALTO=Accessrecord.objects.filter(date__day=15)
     ALTO=Accessrecord.objects.filter(date__year=2025)

     d={'ALTO':ALTO}
     
     return render(request,'display_accessrecord.html',d)



def insert_Topic(request):
     tn=input('enter a topic name: ')

     cto=Topic.objects.get_or_create(topic_name=tn)[0]
     cto.save()

    #  return HttpResponse('topic is inserted successfully')
     
     QLTO=Topic.objects.all()
     d={'QLTO':QLTO}

     return render(request,'display_topic.html',context=d)

def insert_Webpage(request):
     tn=input('enter a topic name: ')
     n=input('enter name: ')
     u=input('enter a url: ')
     e=input('enter an email: ')
     w=Topic.objects.get(topic_name=tn)
    

     c=Webpage.objects.get_or_create(topic_name=w,name=n,url=u,email=e)[0]
     c.save()
      
     WLTO=Webpage.objects.all()
     
     d={'WLTO':WLTO}
     return render(request,'display_webpage.html',context=d)
     return HttpResponse('data is inserted successfully')

def insert_Accessrecord(request):
     pk=int(input('enter pk value of webpage: '))
     
     author=input('enter author: ')
     date=input('enter date: ')
     wo=Webpage.objects.get(pk=pk)
     w=Accessrecord.objects.get_or_create(name=wo,author=author,date=date)[0]
     w.save()
     
     # return HttpResponse('data is inserted successfully!!!!!!!!1')

     ALTO=Webpage.objects.all()
     d={'ALTO':ALTO}






     return render(request,'display_accessrecord.html',context=d)

     