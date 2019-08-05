# Generated by Django 2.2.2 on 2019-08-05 17:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('num', models.IntegerField(default=0)),
                ('goods_name', models.CharField(default='', max_length=50)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
