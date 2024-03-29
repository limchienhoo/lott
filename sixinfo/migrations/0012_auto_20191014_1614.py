# Generated by Django 2.2.6 on 2019-10-14 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sixinfo', '0011_auto_20191014_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zodiac',
            name='name',
            field=models.CharField(choices=[('鸡', '鸡'), ('牛', '牛'), ('龙', '龙'), ('虎', '虎'), ('蛇', '蛇'), ('马', '马'), ('狗', '狗'), ('鼠', '鼠'), ('猴', '猴'), ('猪', '猪'), ('兔', '兔'), ('羊', '羊')], max_length=12, verbose_name='生肖'),
        ),
        migrations.AlterField(
            model_name='zodiac',
            name='qqsh',
            field=models.CharField(choices=[('SHU', '书肖'), ('QI', '棋肖'), ('HUA', '画肖'), ('QING', '琴肖')], max_length=10, verbose_name='琴棋书画肖'),
        ),
        migrations.AlterField(
            model_name='zodiac',
            name='season',
            field=models.CharField(choices=[('SPRING', '春肖/东肖/风肖'), ('AUTUMN', '夏肖/西肖/雷肖'), ('WINTER', '冬肖/北肖/雨肖'), ('SUMMER', '秋肖/南肖/云肖')], max_length=12, verbose_name='春夏秋冬肖'),
        ),
        migrations.AlterField(
            model_name='zodiac',
            name='z_five_element',
            field=models.CharField(choices=[('Z_METAL', '金肖'), ('Z_WOOD', '木肖'), ('Z_FIRE', '火肖'), ('Z_EARTH', '土肖'), ('Z_WATER', '水肖')], max_length=10, verbose_name='五行肖'),
        ),
    ]
