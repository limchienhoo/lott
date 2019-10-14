from django.contrib import admin
from  .models import Zodiac,Haoma



@admin.register(Haoma)
class HaomaAdmin(admin.ModelAdmin):
       list_display = ('name','zodiacs','five_element','head','tail','comp','s_or_d')
       fields = (
            ('name','zodiacs'), 
            ('five_element','boo','s_or_d'),
            ('head','tail','comp')
            )


@admin.register(Zodiac)
class ZodiacAdmin(admin.ModelAdmin):
    list_display = ('name','z_order','sex','heaven_or_earth','nature','home','qqsh','season','z_five_element')
    fields = ('name','z_order','sex','heaven_or_earth','nature','home','qqsh','season','z_five_element')
