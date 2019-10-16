from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import  get_template
from sixinfo.models import Haoma,Zodiac
from pick import models




def get_list_main_ids(request,template,all_zodiacs,all_haomas):

    list_main_ids = []
    list_main_ma_ids = []
    list_main_conditions = dict()
    list_main_ma_conditions = dict()
    template = template
    is_main_pick = False
    is_main_ma_pick = False

    try:
        zo_sex = request.GET['zo_sex']
    except:
        zo_sex = []
    if zo_sex:
        list_main_conditions['sex']=zo_sex

    try:
        zo_home = request.GET['zo_home']
    except:
        zo_home= []
    if zo_home:
        list_main_conditions['home']=zo_home       

    try:
        zo_heaven = request.GET['zo_heaven']
    except:
        zo_heaven= []
    if zo_heaven:
        list_main_conditions['heaven_or_earth']=zo_heaven

    try:
        zo_nature = request.GET['zo_nature']
    except:
        zo_nature= []
    if zo_nature:
        list_main_conditions['nature']=zo_nature

    try:
        ma_sord = request.GET['ma_sord']
    except:
        ma_sord= []
    if ma_sord:
        list_main_ma_conditions['s_or_d']=ma_sord
        
    
    if list_main_conditions:
        is_main_pick = True
        for zodiac in  all_zodiacs.filter(**list_main_conditions):
            for haoma in zodiac.haoma_set.all().order_by('id'):
                list_main_ids.append(haoma.id)

    if list_main_ma_conditions:
        is_main_ma_pick = True
        for haoma in  all_haomas.filter(**list_main_ma_conditions):
                list_main_ma_ids.append(haoma.id)


    if is_main_pick:
        if is_main_ma_pick:
            list_main_ids = list(set(list_main_ids).intersection(set(list_main_ma_ids)))
        else:
            list_main_ids = list_main_ids
    else:
        if is_main_ma_pick:
            list_main_ids = list_main_ma_ids
        else: 
            list_main_ids = []

    is_main_ma_pick = False
    is_main_pick = False

    return list_main_ids


def get_list_ids(request,template,all_zodiacs,zo_pick):
    # qqsh
    list_haoma_ids = []
    zodiacs = []
    template = template
    zo_picks = []
    try:
        if zo_pick == 'qqsh':
            zo_picks = request.GET.getlist('zo_qqsh')
        if zo_pick == 'z_element':
            zo_picks = request.GET.getlist('zo_element')
        if zo_pick == 'season':
            zo_picks = request.GET.getlist('zo_season')
        if zo_pick == 'zodiac':
            zo_picks = request.GET.getlist('zo_zo')
    except:
        zo_picks = []

    if zo_picks:
        if zo_pick == 'qqsh':
            zodiacs_pick = all_zodiacs.filter(qqsh__in=zo_picks)
        if zo_pick == 'z_element':
            zodiacs_pick = all_zodiacs.filter(z_five_element__in=zo_picks)
        if zo_pick == 'season':
            zodiacs_pick = all_zodiacs.filter(season__in=zo_picks)
        if zo_pick == 'zodiac':
            zodiacs_pick = all_zodiacs.filter(name__in=zo_picks)
        for zodiac in zodiacs_pick:
            for haoma in zodiac.haoma_set.all().order_by('id'):
                list_haoma_ids.append(haoma.id)
    else:
        list_haoma_ids = []
    return list_haoma_ids



def get_list_ma_ids(request,template,all_haomas,ma_pick):
    # qqsh
    list_haoma_ids = []
    haomas = []
    template = template
    ma_picks = []
    try:
        if ma_pick == 'boo':
            ma_picks = request.GET.getlist('ma_boo')
        if ma_pick == 'element':
            ma_picks = request.GET.getlist('ma_element')
        if ma_pick == 'tail':
            ma_picks = request.GET.getlist('ma_tail')
        if ma_pick == 'head':
            ma_picks = request.GET.getlist('ma_head')          
        if ma_pick == 'comp':
            ma_picks = request.GET.getlist('ma_comp')
    except:
        ma_picks = []

    if ma_picks:
        if ma_pick == 'boo':
            haomas_pick = all_haomas.filter(boo__in=ma_picks)
        if ma_pick == 'element':
            haomas_pick = all_haomas.filter(five_element__in=ma_picks)
        if ma_pick == 'head':
            haomas_pick = all_haomas.filter(head__in=ma_picks)
        if ma_pick == 'tail':
            haomas_pick = all_haomas.filter(tail__in=ma_picks)
        if ma_pick == 'comp':
            haomas_pick = all_haomas.filter(comp__in=ma_picks)
        for haoma in haomas_pick:
                list_haoma_ids.append(haoma.id)
    else:
        list_haoma_ids = []

    return list_haoma_ids


def set_list_ids(list_all_ids,all_haomas):

    list_set_ids = []
    for haoma in all_haomas:
        list_set_ids.append(haoma.id)
    is_pick = False
    for lists in list_all_ids:
        if lists:
            list_set_ids = list(set(list_set_ids).intersection(set(lists)))
            is_pick = True
    if is_pick == False:
        list_set_ids = []
    return list_set_ids

def pick_haoma(request):

    list_ids = []
    all_haomas = []
    all_zodiacs = []
    haomas_list = []
    zodiacs_list = []
    haomas_list2 = []
    list_all_ids = []

    template = get_template('pick/pick_haoma.html') 
    haomas_list = Haoma.objects.all().order_by('id')
    zodiacs_list = Zodiac.objects.all().order_by('z_order')
    all_zodiacs = zodiacs_list
    all_haomas = haomas_list

    list_main_ids = get_list_main_ids(request,template,all_zodiacs,all_haomas)
    list_all_ids.append(list_main_ids)
    list_qqsh_ids = get_list_ids(request,template,all_zodiacs,zo_pick='qqsh')
    list_all_ids.append(list_qqsh_ids)
    list_season_ids = get_list_ids(request,template,all_zodiacs,zo_pick='season')
    list_all_ids.append(list_season_ids)
    list_z_element_ids = get_list_ids(request,template,all_zodiacs,zo_pick='z_element')
    list_all_ids.append(list_z_element_ids)
    list_zodiac_ids = get_list_ids(request,template,all_zodiacs,zo_pick='zodiac')
    list_all_ids.append(list_zodiac_ids)
    list_boo_ids = get_list_ma_ids(request,template,all_haomas,ma_pick='boo')
    list_all_ids.append(list_boo_ids)
    list_head_ids = get_list_ma_ids(request,template,all_haomas,ma_pick='head')
    list_all_ids.append(list_head_ids)
    list_tail_ids = get_list_ma_ids(request,template,all_haomas,ma_pick='tail')
    list_all_ids.append(list_tail_ids)
    list_comp_ids = get_list_ma_ids(request,template,all_haomas,ma_pick='comp')
    list_all_ids.append(list_comp_ids)
    list_element_ids = get_list_ma_ids(request,template,all_haomas,ma_pick='element')
    list_all_ids.append(list_element_ids)

    list_ids = set_list_ids(list_all_ids,all_haomas)

    for zodiac in zodiacs_list:
        haomas = []
        haoma_list2=[]
        haomas=zodiac.haoma_set.filter(zodiacs=zodiac)
        for haoma in haomas:
            if haoma.id in list_ids:
                haoma.be_pick = True
            else:
                haoma.be_pick = False
            haoma_list2.append(haoma)
        haomas_list2.append(haoma_list2)

    haoma_dict = dict(zip(zodiacs_list,haomas_list2))
    context = {
        'haoma_dict':haoma_dict
    }

    # zo_conditions = {}
    # ma_conditions = {}
    # form = template.select_haoma(request.POST)
    # if request.method == 'POST':
    #     form.save
        
    return render(request,'pick/pick_haoma.html',locals())


    