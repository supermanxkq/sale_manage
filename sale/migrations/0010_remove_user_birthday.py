# Generated by Django 2.2.2 on 2019-07-10 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0009_user_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthday',
        ),
    ]
