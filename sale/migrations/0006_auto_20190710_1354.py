# Generated by Django 2.2.2 on 2019-07-10 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0005_auto_20190710_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(auto_now=True),
        ),
    ]
