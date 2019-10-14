from django.shortcuts import render
from django.http import HttpResponse
from sixinfo.models import Haoma,Zodiac

# Create your views here.

def pick_haoma(request):
    zodiac_ids = []
    haoma_ids = []
    haoma_list = []
    zodiac_list = []
    haomas = []
    haoma_dict = {}
    zodiacs = Zodiac.objects.all()
    for zodiac in zodiacs:
        haomas=Haoma.objects.filter(zodiacs=zodiac)
        if zodiac.id in zodiac_ids:
            zodiac.be_pick = True
            for haoma in haomas:
                haoma.be_pick = True
        zodiac_list.append(zodiac)
        haoma_list2=[]
        for haoma in haomas:
            if haoma.id in haoma_ids:
                haoma.be_pick = True
            haoma_list2.append(haoma)
        haoma_list.append(haoma_list2)
        haomas = []
    haoma_dict = dict(zip(zodiac_list,haoma_list))
    context = {
        'haoma_dict':haoma_dict
    }

    return render(request,'pick/haoma_list.html',context=context)


    