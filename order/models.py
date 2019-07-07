from django.db import models
import django.utils.timezone as timezone
from sale.models import User
from customer.models import Customer

# 订单表
class Order(models.Model):
    order_code=models.CharField(max_length=50,default='')
    status = models.CharField(max_length=5, default='')
    create_time = models.DateTimeField(default=timezone.now)
    bussnessDate = models.DateField(default=timezone.now)
    user_id = models.ForeignKey(User, related_name='order_user_id', on_delete=models.CASCADE)
    mark = models.CharField(max_length=100, default='')
    total_price = models.DecimalField(decimal_places=2, max_digits=10)
    customer_id = models.ForeignKey(Customer, related_name='customer_id', on_delete=models.CASCADE)
    delivery=models.CharField(max_length=100, default='')



