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
from sale import views

app_name = "sale"
urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^loginPage/$', views.login_page,name='login_page'),
    url(r'^login/$', views.login,name='login'),
    url(r'^index/$', views.index,name='index'),
    url(r'^toSignUp/$', views.to_sign_up,name='to_sign_up'),
    url(r'^signUp/$', views.sign_up,name='sign_up'),
    url(r'^logout/$',views.my_logout, name='my_logout'),
    url(r'^toUserInfo/$',views.to_person_info, name='to_person_info'),
    url(r'^getUserInfo/$',views.get_user_info, name='get_user_info'),
]
