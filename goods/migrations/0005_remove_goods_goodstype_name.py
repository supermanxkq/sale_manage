# Generated by Django 2.2.2 on 2019-08-07 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_remove_goods_wholesale_pice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='goodsType_Name',
        ),
    ]
