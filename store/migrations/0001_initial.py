# Generated by Django 2.2.2 on 2019-07-07 08:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(max_length=10)),
                ('num', models.IntegerField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('single_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='store_goods_id', to='goods.Goods')),
            ],
        ),
    ]
