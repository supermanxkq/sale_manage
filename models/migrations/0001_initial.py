# Generated by Django 2.2.2 on 2019-08-10 21:40

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import system.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('img', models.ImageField(default='', upload_to='img')),
                ('phone', models.CharField(default='', max_length=11, unique=True)),
                ('birthday', models.DateField(auto_now_add=True)),
                ('interests', models.CharField(default='', max_length=100)),
                ('address', models.CharField(default='', max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Desk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('status', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('status', models.CharField(default='', max_length=2)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('single_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('img', models.ImageField(storage=system.storage.ImageStorage(), upload_to='img/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('description', models.CharField(default='', max_length=500)),
                ('code', models.CharField(default='', max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.CharField(default='', max_length=50, unique=True)),
                ('status', models.CharField(default='', max_length=5)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('bussnessDate', models.DateField(default=django.utils.timezone.now)),
                ('mark', models.CharField(default='', max_length=100)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_profit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('delivery', models.CharField(default='', max_length=100)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(max_length=20)),
                ('num', models.IntegerField()),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('goodsType_Name', models.CharField(default='', max_length=20)),
                ('goodsType_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_detail_goods_type_id', to='models.GoodsType')),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_detail_goods_id', to='models.Goods')),
                ('order_id', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, related_name='order_detail_order_id', to='models.Order', to_field='order_code')),
            ],
        ),
        migrations.CreateModel(
            name='Msg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('level', models.CharField(default='', max_length=10)),
                ('num', models.IntegerField(default=0)),
                ('goods_name', models.CharField(default='', max_length=100)),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msg_goods_id', to='models.Goods')),
            ],
        ),
        migrations.AddField(
            model_name='goods',
            name='goodsType_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods_goods_type_id', to='models.GoodsType'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('num', models.IntegerField(default=0)),
                ('goods_name', models.CharField(default='', max_length=50)),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cr_us_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_user_id', to=settings.AUTH_USER_MODEL)),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_goods_id', to='models.Goods')),
            ],
        ),
    ]
