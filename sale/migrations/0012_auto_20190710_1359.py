# Generated by Django 2.2.2 on 2019-07-10 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0011_user_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(auto_now_add=True),
        ),
    ]
