# Generated by Django 2.2.6 on 2019-10-10 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sixinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zodiac',
            name='name',
            field=models.CharField(choices=[('鸡', '鸡'), ('兔', '兔'), ('猪', '猪'), ('蛇', '蛇'), ('牛', '牛'), ('虎', '虎'), ('龙', '龙'), ('马', '马'), ('羊', '羊'), ('猴', '猴'), ('狗', '狗'), ('鼠', '鼠')], max_length=12, verbose_name='生肖'),
        ),
        migrations.AlterField(
            model_name='zodiac',
            name='qqsh',
            field=models.CharField(choices=[('QING', '琴肖'), ('QI', '棋肖'), ('HUA', '画肖'), ('SHU', '书肖')], max_length=10, verbose_name='琴棋书画肖'),
        ),
        migrations.AlterField(
            model_name='zodiac',
            name='season',
            field=models.CharField(choices=[('SUMMER', '秋肖/南肖/云肖'), ('SPRING', '春肖/东肖/风肖'), ('WINTER', '冬肖/北肖/雨肖'), ('AUTUMN', '夏肖/西肖/雷肖')], max_length=12, verbose_name='春夏秋冬肖'),
        ),
        migrations.AlterField(
            model_name='zodiac',
            name='z_five_element',
            field=models.CharField(choices=[('Z_EARTH', '土肖'), ('Z_WOOD', '木肖'), ('Z_WATER', '水肖'), ('Z_METAL', '金肖'), ('Z_FIRE', '火肖')], max_length=10, verbose_name='五行肖'),
        ),
    ]