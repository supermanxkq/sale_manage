from msg.models import Msg
from store.models import Store
from django.db.models import Sum
from goods.models import Goods


def  store_watch():
    # 如果库存的数量小于10，就向信息表中插入数据
    nums=Store.objects.values('goods_id_id','goods_name').annotate(number=Sum("num"))
    if nums:
        for item in nums:
            if item['number']<= 10:
                msgs=Msg.objects.filter(goods_id=item['goods_id_id'])
                if  len(msgs)==0:
                    Msg.objects.create(name='库存不足报警',level='danger',num=item['number'],goods_name=item['goods_name'],goods_id_id=item['goods_id_id'])
            else:
                Msg.objects.filter(goods_id=item['goods_id_id']).delete()

    goods_list=Goods.objects.filter(status='ZC')
    for goods in goods_list:
        storeQuerySet=Store.objects.filter(goods_id_id=goods.id)
        if not storeQuerySet:
            msgs = Msg.objects.filter(goods_id=goods.id)
            if len(msgs) == 0:
                Msg.objects.create(name='无库存', level='danger', num=0, goods_name=goods.name,
                                   goods_id_id=goods.id)
        else:
            Msg.objects.filter(goods_id=goods.id).delete()
