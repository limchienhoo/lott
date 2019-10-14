from django.db import models
from sixinfo.models import Zodiac,Haoma

# Create your models here.
class  Issue(models.Model):
    
    issue_num = models.CharField(max_length=10,verbose_name="期号")
    issue_opentime = models.DateTimeField(auto_now_add=False,verbose_name="每期开奖时间")
    is_opened = models.BooleanField(default=False,verbose_name="是否开过")
    issue_haoma = models.ForeignKey(Haoma,verbose_name="開獎特碼",on_delete=None)

    def __str__(self):
        return self.issue_num

    class Meta:
        verbose_name = verbose_name_plural = "全年期号以及开奖时间表"

class Sysdata(models.Model):
    
    sys_zodiac = models.ForeignKey(Zodiac,verbose_name="系统当前年肖",on_delete=None)
    is_conf = models.BooleanField(default=False,verbose_name="是否**")

    # def change_zodiac(self):
        
        # hoamas = Haoma
        # # if sys_zodiac != Haoma.object.Ma1.zodiac:
            # for haomas in 
    #         exit

    # def  __str__(self):
    #      return self.sys_zodiac

    class Meta:
        verbose_name = verbose_name_plural = "系统生肖"