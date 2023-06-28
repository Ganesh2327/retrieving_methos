from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.
def insert_Topic(request):
    TN=input('enter name= ')
    TO=Topic.objects.get_or_create(topic_name=TN)[0]
    TO.save()
    return HttpResponse('tpoic is created')



def insert_Webpage(request):
    TN=input('enter topic name= ')
    TO=Topic.objects.get_or_create(topic_name=TN)[0]
    TO.save()
    N=input('enter name= ')
    U=input('enter url= ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=N,url=U)[0]
    WO.save()
    return HttpResponse('webpage is created')
    
def insert_AccessRecords(request):
    TN=input('enter topic name= ')
    TO=Topic.objects.get_or_create(topic_name=TN)[0]
    TO.save()
    N=input('enter name= ')
    U=input('enter url= ')
    D=input('enter date= ')
    A=input('enter author= ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=N,url=U)[0]
    WO.save()
 
    AR=AccessRecords.objects.get_or_create(name=WO,date=D,author=A)[0]
    AR.save()
    return HttpResponse('AccessRecords are created')




def display_topics(request):
    Topics=Topic.objects.all()
    Topics=Topic.objects.filter(topic_name='cricket')
    #Topics=Topic.objects.get(topic_name='cricket') 
    Topics=Topic.objects.all()
    Topics=Topic.objects.all().order_by('topic_name')
    Topics=Topic.objects.all().order_by('-topic_name') 
    Topics=Topic.objects.exclude(topic_name='cricket')  
    Topics=Topic.objects.all().order_by(Length('topic_name'))
    Topics=Topic.objects.all().order_by(Length('topic_name'))
    
    d={'Topics':Topics}
    return render(request,'display_topics.html',d)


def display_webpages(request):
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.all().order_by('name')
    #webpages=Webpage.objects.filter(startwith='G')
    webpages=Webpage.objects.filter(name='Ganesh')
    webpages=Webpage.objects.all().order_by(Length('name'))
    webpages=Webpage.objects.exclude(name='virat')
    webpages=Webpage.objects.order_by('-name')
    webpages=Webpage.objects.order_by(Length('name'))
    #webpages=Webpage.objects.order_by(Length('name').asc)
    webpages=Webpage.objects.all()
    webpages=Webpage.objects.filter(Q(name='Virat') | Q(url__startswith='https'))
    webpages=Webpage.objects.filter(Q(name='Rahul') & Q(url__startswith='https'))
    webpages=Webpage.objects.filter(name__in=['virat','Ganesh'])
    webpages=Webpage.objects.filter(name__regex='G\w+')
    webpages=Webpage.objects.all()
  
    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)


def display_AccessRecords(request):
    AccessRecordss=AccessRecords.objects.all()
    AccessRecordss=AccessRecords.objects.filter(date__year='2023')
    AccessRecordss=AccessRecords.objects.filter(date__month='06')
    AccessRecordss=AccessRecords.objects.filter(date__day='14')
    AccessRecordss=AccessRecords.objects.filter(date__day='5')
    AccessRecordss=AccessRecords.objects.filter(date__gt='2010-06-29')
    AccessRecordss=AccessRecords.objects.filter(date__lt='2010-06-29')
    AccessRecordss=AccessRecords.objects.filter(date__gte='2010-06-29')
    AccessRecordss=AccessRecords.objects.filter(date__lte='2010-06-29')

    d={'AccessRecordss':AccessRecordss}
    return render(request,'display_AccessRecords.html',d)


def update_webpages(request):

    webpages=Webpage.objects.filter(name='Ganesh').update(url='https://gan.in')
    webpages=Webpage.objects.filter(topic_name='football').update(url='https://FT.in')
    Webpage.objects.filter(name='virat').update(url='https://vk.in')
    Webpage.objects.filter(name='Dhoni').update(topic_name='BCCI Cricket')
    Webpage.objects.filter(name='messi').update(topic_name='football')
    Webpage.objects.update_or_create(name='virat',defaults={'url':'http://VIRATKING.com'})
    Webpage.objects.update_or_create(topic_name='chess',defaults={'url':'http://chess.com'})
    Webpage.objects.update_or_create(name='prasad',defaults={'url':'http://pk.com'})
    #Webpage.objects.update_or_create(name='Pandya',defaults={'topic_name':Topic,'url':'http://pandya.com'})
    webpages=Webpage.objects.all()
    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)



def delete_webpages(request):
    
    webpages=Webpage.objects.all()

    webpages=Webpage.objects.filter(name='Ganesh').delete()

    webpages=Webpage.objects.all().delete()

    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)






