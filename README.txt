pip install pymysql
pip install django_crontab
pip install xlwt
注释mysql version
pip install Pillow

decode -->encode

mysql remote connect

grant all privileges on *.* to 'root'@'%' identified by '0808XuKaiQiang..' with grant option;
flush privileges;

0 rows


PyQtWebEngine


使用pyQT打印热敏小票

一、采用html模板进行打印
    问题：不能直接进行打印、数据不能进行渲染

二、直接进行打印
    问题：打印的样式比较模糊、可以进行直接打印