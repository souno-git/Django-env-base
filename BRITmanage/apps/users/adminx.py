import xadmin
from xadmin import views
from .models import UserProfile


class UsersAdmin(object):
    list_display = ['username', 'name', 'birthday', 'mobile', 'gender', 'email', 'q_number']
    search_fields = ['username', 'name', 'mobile', 'gender', 'email']
    list_filter = ['username', 'name', 'birthday', 'mobile', 'gender', 'email', 'q_number']


class GlobalSettings(object):
    site_title = "佰润 IT 管理系统"
    site_footer = "Souno.cn All rights reserved; those responsible for unauthorized reproduction will be prosecuted。"


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile, UsersAdmin)
