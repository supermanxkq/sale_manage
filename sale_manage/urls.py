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
from merchant import views as merchant_view
from customer import views as customer_view
from goods import views as goods_view
from store import views as store_view
from msg import views as msg_view
from order import views as order_view
from orderdetail import views as  order_detail_view
from home import views as home_view

app_name = "sale"
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^loginPage/$', sale_view.login_page, name='login_page'),
    url(r'^login/$', sale_view.login, name='login'),
    url(r'^$', sale_view.index),
    url(r'^toSignUp/$', sale_view.to_sign_up, name='to_sign_up'),
    url(r'^signUp/$', sale_view.sign_up, name='sign_up'),
    url(r'^logout/$', sale_view.my_logout, name='my_logout'),
    # url(r'^toUserInfo/$',views.to_person_info, name='to_person_info'),
    url(r'^getUserInfo/$', sale_view.get_user_info, name='get_user_info'),
    url(r'^updateUserInfo/$', sale_view.update_user_info, name='update_user_info'),
    url(r'^updatePwd/$', sale_view.updatePwd, name='updatePwd'),
    url(r'^toUpPwd/$', sale_view.toUpPwd, name='toUpPwd'),

    # 商品类型管理
    url(r'^goodsTypeList/$', sale_view.goodsTypeList, name='goodsTypeList'),
    url(r'^delGoodsType/(?P<id>[0-9]+)$', sale_view.del_goods_type, name='del_goods_type'),
    url(r'^goodstype_edit/(?P<id>[0-9]+)$', sale_view.goodstype_edit, name='goodstype_edit'),
    url(r'^updateGoodstype/$', sale_view.goodstype_update, name='goodstype_update'),
    url(r'^to_add_goods_type/$', sale_view.to_add_goods_type, name='to_add_goods_type'),
    url(r'^goods_type_add/$', sale_view.goods_type_add, name='goods_type_add'),
    url(r'^list_page/$', merchant_view.list_page, name='list_page'),
    url(r'^query_goodstype_list/$', sale_view.query_goodstype_list, name='query_goodstype_list'),
    # 供应商管理
    url(r'^toAdd/$', merchant_view.toAdd, name='toAdd'),
    url(r'^add/$', merchant_view.add, name='add'),
    url(r'^export/$', merchant_view.export, name='export'),
    url(r'^check_login/$', sale_view.check_login, name='check_login'),
    url(r'^delete/(?P<id>[0-9]+)$', merchant_view.delete, name='delete'),
    url(r'^queryMerchants/$', merchant_view.queryMerchants, name='queryMerchants'),
    # 客户管理
    url(r'^customer_list_page/$', customer_view.list_page, name='customer_list_page'),
    url(r'^delete_customer/(?P<id>[0-9]+)$', customer_view.delete, name='delete_customer'),
    url(r'^toCustomerAdd/$', customer_view.toAdd, name='toCustomerAdd'),
    url(r'^add_customer/$', customer_view.add, name='add_customer'),
    url(r'^export_customer/$', customer_view.export, name='export_customer'),
    url(r'^query_customer_list/$', customer_view.query_customer_list, name='query_customer_list'),
    # 商品管理
    url(r'^goods_list_page/$', goods_view.list_page, name='goods_list_page'),
    url(r'^delete_goods/(?P<id>[0-9]+)$', goods_view.delete, name='delete_goods'),
    url(r'^toGoodsAdd/$', goods_view.toAdd, name='toGoodsAdd'),
    url(r'^add_goods/$', goods_view.add, name='add_goods'),
    url(r'^queryGoodsNameList/$', goods_view.queryGoodsNameList, name='queryGoodsNameList'),
    url(r'^queryGoodsById/$', goods_view.queryGoodsById, name='queryGoodsById'),
    #  库存管理
    url(r'^store_list_page/$', store_view.list_page, name='store_list_page'),
    url(r'^delete_store/(?P<id>[0-9]+)$', store_view.delete, name='delete_store'),
    url(r'^toStoreAdd/$', store_view.toAdd, name='toStoreAdd'),
    url(r'^add_store/$', store_view.add, name='add_store'),
    #  预警信息管理
    url(r'^queryMsgList/$', msg_view.queryMsgList, name='queryMsgList'),

    #  订单管理
    url(r'^queryOrderList/$', order_view.queryOrderList, name='queryOrderList'),
    url(r'^delete_order/(?P<id>[0-9]+)$', order_view.delete, name='delete_order'),
    url(r'^toOrderAdd/$', order_view.toAdd, name='toOrderAdd'),
    url(r'^add_order/$', order_view.add_order, name='add_order'),
    url(r'^queryTodayOrders/$', order_view.queryTodayOrder, name='queryTodayOrders'),

    # 订单详情管理
    url(r'^queryOrderDetailList/(?P<order_code>[0-9]+)$', order_detail_view.queryOrderDetailList, name='queryOrderDetailList'),

    # 首页
    url(r'^queryStatisticsData/$', home_view.queryStatisticsData,
        name='queryStatisticsData'),

]
