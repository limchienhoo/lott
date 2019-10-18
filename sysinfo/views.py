from django.shortcuts import render
from sixinfo.models import Haoma,Zodiac
from datetime import datetime

# Create your views here.
def homepage(request):

    haomas = Haoma.objects.all().order_by('id')
    zodiacs = Zodiac.objects.all().order_by('z_order')

    return render(request,'index.html',locals())