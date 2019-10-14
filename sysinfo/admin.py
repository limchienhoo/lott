from django.contrib import admin
from  .models import  Issue,Sysdata

# Register your models here.

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
       list_display = ('issue_num','issue_opentime','is_opened','issue_haoma')
       fields = (
            ('issue_num'), 
            ('issue_opentime','is_opened','issue_haoma')
            )

# @admin.register(Sysdata)
# class SysdataAdmin(admin.ModelAdmin):
#        list_display = ('is_conf ','sys_zodiac')
#        fields = (
#             ('is_conf'), 
#             ('sys_zodiac')
#             )