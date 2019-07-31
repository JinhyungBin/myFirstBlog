from django.shortcuts import render
from .models import Portfolio, TravelsA, TravelsC, TravelsL


#전체 사진을 보고 싶음
def popol(request):
    portfolios=Portfolio.objects
    return render(request,'popol.html',{'portfolios':portfolios})

#여행 사진 여러장 올릴곳
def travelChina(request):
    tc=TravelsC.objects
    return render(request,'travelChina.html',{'tc':tc})

def travelLaos(request):
    tl=TravelsL.objects
    return render(request,'travelLaos.html',{'tl':tl})

def travelAmerica(request):
    ta=TravelsA.objects
    return render(request,'travelAmerica.html',{'ta':ta})

def test(request): #new.html을 띄워주는 함수
    return render(request, 'test.html')
