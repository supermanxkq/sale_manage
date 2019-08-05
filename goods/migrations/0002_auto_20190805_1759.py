# Generated by Django 2.2.2 on 2019-08-05 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('merchant', '0001_initial'),
        ('sale', '0001_initial'),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goodsType_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_goods_type_id', to='sale.GoodsType'),
        ),
        migrations.AddField(
            model_name='goods',
            name='merchant_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_mer_id', to='merchant.Merchant'),
        ),
    ]
