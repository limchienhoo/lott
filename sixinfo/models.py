import sys
from django.db import models
from django.contrib.auth.models import User



class Zodiac(models.Model):
 
    ZODIAC_CHOIES = {
        ('鼠', '鼠'),
        ('牛', '牛'),
        ('虎', '虎'),
        ('兔', '兔'),
        ('龙' ,'龙'),
        ('蛇', '蛇'),
        ('马', '马'),
        ('羊', '羊'),
        ('猴', '猴'),
        ('鸡', '鸡'),
        ('狗', '狗'),
        ('猪', '猪'),
     }

    QQSH_CHOIES={
        ('QING','琴肖'),
        ('QI', '棋肖'),
        ('SHU', '书肖'),
        ('HUA', '画肖'),
    }

    SEASON_CHOIES={
        ('SPRING',  '春肖/东肖/风肖'),
        ('AUTUMN', '夏肖/西肖/雷肖'),
        ('SUMMER', '秋肖/南肖/云肖'),
        ('WINTER', '冬肖/北肖/雨肖'),
    }


    Z_ELEMENT_CHOIES = {
        ('Z_METAL',  '金肖'),
        ('Z_WOOD', '木肖'),
        ('Z_WATER', '水肖'),
        ('Z_FIRE',  '火肖'),
        ('Z_EARTH', '土肖'),
     }

    # sequence = models.CharField()
    name = models.CharField(max_length=12,choices=ZODIAC_CHOIES,verbose_name="生肖")
    sex = models.BooleanField(default=True,verbose_name="是否男肖")
    heaven_or_earth =models.BooleanField(default=True,verbose_name="是否天肖")
    nature = models.BooleanField(default=True,verbose_name="是否阳肖")
    home = models.BooleanField(default=True,verbose_name="是否家肖")
    qqsh = models.CharField(max_length=10,choices=QQSH_CHOIES,verbose_name="琴棋书画肖")
    season = models.CharField(max_length=12,choices=SEASON_CHOIES,verbose_name="春夏秋冬肖")
    z_five_element = models.CharField(max_length=10,choices=Z_ELEMENT_CHOIES,verbose_name="五行肖")
    z_order = models.PositiveIntegerField(default=0,verbose_name="生肖序号")

    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name = verbose_name_plural = "生肖"



class Haoma(models.Model):

    MA_CHOIES = (
        ('01', '01'),
        ('02', '02'),
        ('03', '03'),
        ('04', '04'),
        ('05', '05'),
        ('06', '06'),
        ('07', '07'),
        ('08', '08'),
        ('09', '09'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13' , '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
        ('19', '19'),
        ('20', '20'),
        ('21', '21'),
        ('22', '22'),
        ('23', '23'),
        ('24', '24'),
        ('25', '25'),
        ('26', '26'),
        ('27', '27'),
        ('28', '28'),
        ('29', '29'),
        ('30', '30'),
        ('31', '31'),
        ('32', '32'),
        ('33', '33'),
        ('34', '34'),
        ('35', '35'),
        ('36', '36'),
        ('37', '37'),
        ('38', '38'),
        ('39', '39'),
        ('40', '40'),
        ('41', '41'),
        ('42', '42'),
        ('43', '43'),
        ('44', '44'),
        ('45', '45'),
        ('46', '46'),
        ('47', '47'),
        ('48', '48'),
        ('49', '49'),
    )

    FIVE_CHOIES = (
        ('METAL' , '金'),
        ('WOOD' , '木'),
        ('WATER' , '水'),
        ('FIRE ', '火'),
        ('EARTH ', '土'),
    )

    BOO_CHOIES = (
        ('RED_S' , '红单'),
        ('RED_D' , '红双'),
        ('BLUE_S' , '蓝单'),
        ('BLUE_D' , '蓝双'),
        ('GREEN_S' , '绿单'),
        ('GREEN_D' , '绿双'),
    )

    SORD_SINGLE = 1
    SORD_DOUBLE = 2
    SORD_ITEMS = (
        (SORD_SINGLE , '单数'),
        (SORD_DOUBLE , '双数'),
    )

    HEAD_CHOIES = (
        ('HEAD_0' , '0头'),
        ('HEAD_1' , '1头'),
        ('HEAD_2' , '2头'),
        ('HEAD_3' , '3头'),
        ('HEAD_4' , '4头'),
    )

    TAIL_CHOIES = (
        ('TAIL_0' , '0尾'),
        ('TAIL_1' , '1尾'),
        ('TAIL_2' , '2尾'),
        ('TAIL_3' , '3尾'),
        ('TAIL_4' , '4尾'),
        ('TAIL_5' , '5尾'),
        ('TAIL_6' , '6尾'),
        ('TAIL_7' , '7尾'),
        ('TAIL_8' , '8尾'),
        ('TAIL_9' , '9尾'),
    )

    COMP_CHOIES = (
        ('COMP_1' , '1合'),
        ('COMP_2' , '2合'),
        ('COMP_3' , '3合'),
        ('COMP_4' , '4合'),
        ('COMP_5' , '5合'),
        ('COMP_6' , '6合'),
        ('COMP_7' , '7合'),
        ('COMP_8' , '8合'),
        ('COMP_9' , '9合'),
        ('COMP_10' , '10合'),
        ('COMP_11' , '11合'),
        ('COMP_12' , '12合'),
        ('COMP_13' , '13合'),
    )
    name = models.CharField(max_length=5,choices=MA_CHOIES,verbose_name="号码",unique=True)
    five_element = models.CharField(max_length=10,choices=FIVE_CHOIES,verbose_name="号码五行")
    boo = models.CharField(max_length=10,choices=BOO_CHOIES,verbose_name="号码波色")
    s_or_d = models.PositiveIntegerField(default=0,choices=SORD_ITEMS,verbose_name="号码单双")
    head = models.CharField(max_length=10,choices=HEAD_CHOIES,verbose_name="号码头")
    tail = models.CharField(max_length=10,choices=TAIL_CHOIES,verbose_name="号码尾")
    comp = models.CharField(max_length=10,choices=COMP_CHOIES,verbose_name="号码尾")
    zodiacs = models.ForeignKey(Zodiac,verbose_name="所属生肖",on_delete=None)
    

    @staticmethod
    def get_all_haoma(cls):
        queryset = cls.objects.all()
        return queryset

    # @staticmethod
    # def get_five_element(self,five_element):
    #     try:
    #         pick_haoma = self.objects.filter(five_element=five_element)

    #     pick_haoma = []

        # return pick_haoma 





    def __str__(self):
         return self.name

    class Meta:
        verbose_name = verbose_name_plural = "号码"
        ordering = ['-name']



# class Nlzodiac(models.Model):

#     nl_year= models.CharField(max_length=10,  verbose_name="农历年份")
#     s_datetime = models.DateField(verbose_name="开始日期")
#     e_datetime = models.DateField(verbose_name="结束日期")
#     # the_zodiac = models.ForeignKey(Zodiac,verbose_name="农历年的生肖",on_delete=models.CASCADE)
#     sys_zodiac = models.ForeignKey(Zodiac,verbose_name="当前系统生肖年",on_delete=None)
#     is_sys_zodiac = models.BooleanField(default=False,verbose_name="是否当天生肖") 


    # def __str__(self):
    #     return self.name

    # class Meta:
    #     managed = True
    #     verbose_name = verbose_name_plural = "农历生肖"
    