# Generated by Django 2.2.2 on 2019-07-10 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(default='1992-08-16'),
        ),
    ]
