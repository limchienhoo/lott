from django.shortcuts import render
from django.http import HttpResponse
from sixinfo.models import Haoma,Zodiac

# Create your views here.

def pick_haoma(request):
    haoma_list = []
    zodiac_list = []
    haoma_dict = {}
    zodiacs = Zodiac.objects.all()
    for zodiac in zodiacs:
        zodiac_list.append(zodiac)
        haomas=Haoma.objects.filter(zodiacs=zodiac)
        haoma_list2=[]
        for haoma in haomas:
            haoma_list2.append(haoma.name)
        haoma_list.append(haoma_list2)
    haoma_dict = dict(zip(zodiac_list,haoma_list))
    context = {
        'haoma_dict':haoma_dict
    }

    return render(request,'sixinfo/haoma_list.html',context=context)