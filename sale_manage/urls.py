"""sale_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from sale import views as sale_view
from goods import views as goods_view
from order import views as order_view
from orderdetail import views as  order_detail_view
from home import views as home_view
from msg import views as msg_view
from cart import views as cart_view
from desk import views as desk_view
app_name = "sale"
urlpatterns = [
    url('admin/', admin.site.urls),
    # 用户管理
    url(r'^home/$', sale_view.home, name='home'),
    url(r'^loginPage/$', sale_view.login_page, name='login_page'),
    url(r'^login/$', sale_view.login, name='login'),
    url(r'^toAddUser/$', sale_view.toAddUser, name='toAddUser'),
    url(r'^add_user/$', sale_view.add_user, name='add_user'),
    url(r'^logout/$', sale_view.my_logout, name='my_logout'),
    # url(r'^toUserInfo/$',views.to_person_info, name='to_person_info'),
    url(r'^getUserInfo/$', sale_view.get_user_info, name='get_user_info'),
    url(r'^updateUserInfo/$', sale_view.update_user_info, name='update_user_info'),
    url(r'^updatePwd/$', sale_view.updatePwd, name='updatePwd'),
    url(r'^toUpPwd/$', sale_view.toUpPwd, name='toUpPwd'),
    url(r'^queryUserList/$', sale_view.queryUserList, name='queryUserList'),

    # 商品类型管理
    url(r'^goodsTypeList/$', sale_view.goodsTypeList, name='goodsTypeList'),
    url(r'^delGoodsType/(?P<id>[0-9]+)$', sale_view.del_goods_type, name='del_goods_type'),
    url(r'^goodstype_edit/(?P<id>[0-9]+)$', sale_view.goodstype_edit, name='goodstype_edit'),
    url(r'^updateGoodstype/$', sale_view.goodstype_update, name='goodstype_update'),
    url(r'^to_add_goods_type/$', sale_view.to_add_goods_type, name='to_add_goods_type'),
    url(r'^goods_type_add/$', sale_view.goods_type_add, name='goods_type_add'),
    url(r'^query_goodstype_list/$', sale_view.query_goodstype_list, name='query_goodstype_list'),
    url(r'^queryNameCharacter/$', sale_view.queryNameCharacter, name='queryNameCharacter'),
    # 客户管理

    # 商品管理
    url(r'^goods_list_page/$', goods_view.list_page, name='goods_list_page'),
    url(r'^delete_goods/(?P<id>[0-9]+)$', goods_view.delete, name='delete_goods'),
    url(r'^toGoodsAdd/$', goods_view.toAdd, name='toGoodsAdd'),
    url(r'^add_goods/$', goods_view.add, name='add_goods'),
    url(r'^queryGoodsNameList/$', goods_view.queryGoodsNameList, name='queryGoodsNameList'),
    url(r'^queryGoodsById/$', goods_view.queryGoodsById, name='queryGoodsById'),
    url(r'^goods_edit/(?P<id>[0-9]+)$', goods_view.goods_edit, name='goods_edit'),
    url(r'^goods_update/$', goods_view.goods_update, name='goods_update'),
    #  库存管理
    #  预警信息管理
    url(r'^queryMsgList/$', msg_view.queryMsgList, name='queryMsgList'),

    #  订单管理
    url(r'^queryOrderList/$', order_view.queryOrderList, name='queryOrderList'),
    url(r'^delete_order/(?P<id>[0-9]+)$', order_view.delete, name='delete_order'),
    url(r'^toOrderAdd/$', order_view.toAdd, name='toOrderAdd'),
    url(r'^toOrderFood/$', order_view.toOrderFood, name='toOrderFood'),
    url(r'^add_order/$', order_view.add_order, name='add_order'),
    url(r'^queryTodayOrders/$', order_view.queryTodayOrder, name='queryTodayOrders'),
    url(r'^printOrder/$', order_view.printOrder, name='printOrder'),

    # 订单详情管理
    url(r'^queryOrderDetailList/(?P<order_code>[0-9]+)$', order_detail_view.queryOrderDetailList, name='queryOrderDetailList'),

    # 首页
    url(r'^queryStatisticsData/$', home_view.queryStatisticsData,
        name='queryStatisticsData'),

    # 消息通知
    url(r'^queryMsgListPage/$', msg_view.queryMsgListPage, name='queryMsgListPage'),
    # 购物车
    url(r'^addShopCart/$', cart_view.addShopCart, name='addShopCart'),
    url(r'^query_cart_list/$', cart_view.query_cart_list, name='query_cart_list'),
    url(r'^toConfirmOrder/$', cart_view.toConfirmOrder, name='toConfirmOrder'),
    url(r'^delete_cart/(?P<id>[0-9]+)$', cart_view.delete_cart, name='delete_cart'),
    # 桌台管理
    url(r'^desk_list_page/$', desk_view.desk_list_page, name='desk_list_page'),
    url(r'^to_desk_add/$', desk_view.to_desk_add, name='to_desk_add'),
    url(r'^add_desk/$', desk_view.add_desk, name='add_desk'),
    url(r'^desk_edit/(?P<id>[0-9]+)$', desk_view.desk_edit, name='desk_edit'),
    url(r'^delete_desk/(?P<id>[0-9]+)$', desk_view.delete_desk, name='delete_desk'),
    url(r'^desk_update/$', desk_view.desk_update, name='desk_update'),

]
