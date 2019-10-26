学生体能测试上报辅助系统
作者开发系统：deepin15.11，pycharm2019<br>
软件环境Python3.7 django2.2.6,使用sqlite３数据库

系统的安装过程：
pip install django<br>
在https://github.com/sshwsfc/xadmin/tree/django2下载对应的适应2.0版的xadmin，进入下载目录执行：<br>
pip install xadmin-django2<br>
然后地使用https://github.com/vip68/xadmin_bugfix提供的版本覆盖xadmin的安装目录<br>
安装计算字段包：
pip install django-computed-property<br>
启动软件：
进入工程目录执行：
python manage.py runserver