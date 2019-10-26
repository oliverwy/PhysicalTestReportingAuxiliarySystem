# from django.contrib import admin
import xadmin
from .models import *
from xadmin.views.website import LoginView,LogoutView
from import_export import resources
from xadmin import views
from xadmin.layout import Main, Fieldset, Side
from django.apps import apps

class LoginViewAdmin(LoginView):
    title = '体能测试成绩辅助系统'

class LogOutViewAdmin(LogoutView):
    title = '体能测试成绩辅助系统'
# Register your models here.
class StudentsInfoResource(resources.ModelResource):
    def __init__(self):
        super(StudentsInfoResource, self).__init__()
        field_list = apps.get_model('app', 'Students')._meta.fields
        self.verbose_name_dict = {}
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name
        print(self.verbose_name_dict)

    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            # print(field_name)
            if field_name in self.verbose_name_dict.keys():
                field.colum_name = self.verbose_name_dict[field_name]
        return fields

    class Meta:
        model = Students
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        # 在导入预览页面中显示跳过的记录

        import_id_fields = ('id',)
        # 对象标识的默认字段是id，您可以选择在导入时设置哪些字段用作id

        fields = (
            'gradeclass',
            'classname',
            'address',
            'studentid',
            'name',
            'gender',
            'bithday',
            'idcardno',
            'stature',
            'weight',
            'lungcapacity',
            'fiftymeter',
            'middle_distancerun',
            'sitandreach',
            'standingbroadjump',
            'pull_ups',
            'Oneminutesitups',
            'score',
            'enrollment',
            'remarks',
        )


class ClassInfoResource(resources.ModelResource):
    def __init__(self):
        super(ClassInfoResource, self).__init__()
        field_list = apps.get_model('app', 'Class')._meta.fields
        self.verbose_name_dict = {}
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name
        print(self.verbose_name_dict)

    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            # print(field_name)
            if field_name in self.verbose_name_dict.keys():
                field.colum_name = self.verbose_name_dict[field_name]
        return fields

    class Meta:
        model = Class
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        # 在导入预览页面中显示跳过的记录

        import_id_fields = ('id',)
        # 对象标识的默认字段是id，您可以选择在导入时设置哪些字段用作id

        fields = (
            'class_name',
        )
        # 白名单

        # exclude = (
        #     'create_time',
        #     'update_time',
        # )
        # 黑名单

class LungCapacityTestNormalResource(resources.ModelResource):
    def __init__(self):
        super(LungCapacityTestNormalResource, self).__init__()
        field_list = apps.get_model('app', 'LungCapacityTestNormal')._meta.fields
        self.verbose_name_dict = {}
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name
        print(self.verbose_name_dict)

    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            # print(field_name)
            if field_name in self.verbose_name_dict.keys():
                field.colum_name = self.verbose_name_dict[field_name]
        return fields

    class Meta:
        model = LungCapacityTestNormal
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        # 在导入预览页面中显示跳过的记录

        import_id_fields = ('id',)
        # 对象标识的默认字段是id，您可以选择在导入时设置哪些字段用作id

        fields = (
            'classtype',
            'ItemScore',
            'malefirst',
            'maleSecond',
            'femalefirst',
            'femaleSecond',
        )

class FiftymeterTestNormalResource(resources.ModelResource):
    def __init__(self):
        super(FiftymeterTestNormalResource, self).__init__()
        field_list = apps.get_model('app', 'FiftymeterTestNormal')._meta.fields
        self.verbose_name_dict = {}
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name
        print(self.verbose_name_dict)

    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            # print(field_name)
            if field_name in self.verbose_name_dict.keys():
                field.colum_name = self.verbose_name_dict[field_name]
        return fields

    class Meta:
        model = FiftymeterTestNormal
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        # 在导入预览页面中显示跳过的记录

        import_id_fields = ('id',)
        # 对象标识的默认字段是id，您可以选择在导入时设置哪些字段用作id

        fields = (
            'classtype',
            'ItemScore',
            'malefirst',
            'maleSecond',
            'femalefirst',
            'femaleSecond',
        )


class SitandReachTestNoramlResource(resources.ModelResource):
    def __init__(self):
        super(SitandReachTestNoramlResource, self).__init__()
        field_list = apps.get_model('app', 'FiftymeterTestNormal')._meta.fields
        self.verbose_name_dict = {}
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name
        print(self.verbose_name_dict)

    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            # print(field_name)
            if field_name in self.verbose_name_dict.keys():
                field.colum_name = self.verbose_name_dict[field_name]
        return fields

    class Meta:
        model = SitandReachTestNoraml
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        # 在导入预览页面中显示跳过的记录

        import_id_fields = ('id',)
        # 对象标识的默认字段是id，您可以选择在导入时设置哪些字段用作id

        fields = (
            'classtype',
            'ItemScore',
            'malefirst',
            'maleSecond',
            'femalefirst',
            'femaleSecond',
        )

class StandingBroadJumpTestNormalResource(resources.ModelResource):
    def __init__(self):
        super(StandingBroadJumpTestNormalResource, self).__init__()
        field_list = apps.get_model('app', 'FiftymeterTestNormal')._meta.fields
        self.verbose_name_dict = {}
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name
        print(self.verbose_name_dict)

    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            # print(field_name)
            if field_name in self.verbose_name_dict.keys():
                field.colum_name = self.verbose_name_dict[field_name]
        return fields

    class Meta:
        model = StandingBroadJumpTestNormal
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        # 在导入预览页面中显示跳过的记录

        import_id_fields = ('id',)
        # 对象标识的默认字段是id，您可以选择在导入时设置哪些字段用作id

        fields = (
            'classtype',
            'ItemScore',
            'malefirst',
            'maleSecond',
            'femalefirst',
            'femaleSecond',
        )

class OneMinuteSitupsAndPullUpTestNormalResource(resources.ModelResource):
    def __init__(self):
        super(OneMinuteSitupsAndPullUpTestNormalResource, self).__init__()
        field_list = apps.get_model('app', 'FiftymeterTestNormal')._meta.fields
        self.verbose_name_dict = {}
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name
        print(self.verbose_name_dict)

    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            # print(field_name)
            if field_name in self.verbose_name_dict.keys():
                field.colum_name = self.verbose_name_dict[field_name]
        return fields

    class Meta:
        model = OneMinuteSitupsAndPullUpTestNormal
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        # 在导入预览页面中显示跳过的记录

        import_id_fields = ('id',)
        # 对象标识的默认字段是id，您可以选择在导入时设置哪些字段用作id

        fields = (
            'classtype',
            'ItemScore',
            'malefirst',
            'maleSecond',
            'femalefirst',
            'femaleSecond',
        )

class MiddleDistanceRunTestNormalResource(resources.ModelResource):
    def __init__(self):
        super(MiddleDistanceRunTestNormalResource, self).__init__()
        field_list = apps.get_model('app', 'FiftymeterTestNormal')._meta.fields
        self.verbose_name_dict = {}
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name
        print(self.verbose_name_dict)

    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            # print(field_name)
            if field_name in self.verbose_name_dict.keys():
                field.colum_name = self.verbose_name_dict[field_name]
        return fields

    class Meta:
        model = MiddleDistanceRunTestNormal
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        # 在导入预览页面中显示跳过的记录

        import_id_fields = ('id',)
        # 对象标识的默认字段是id，您可以选择在导入时设置哪些字段用作id

        fields = (
            'classtype',
            'ItemScore',
            'malefirst',
            'maleSecond',
            'femalefirst',
            'femaleSecond',
        )

class MiddleDistanceRunPlusTestNormalResource(resources.ModelResource):
    def __init__(self):
        super(MiddleDistanceRunPlusTestNormalResource, self).__init__()
        field_list = apps.get_model('app', 'FiftymeterTestNormal')._meta.fields
        self.verbose_name_dict = {}
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name
        print(self.verbose_name_dict)

    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            # print(field_name)
            if field_name in self.verbose_name_dict.keys():
                field.colum_name = self.verbose_name_dict[field_name]
        return fields

    class Meta:
        model = MiddleDistanceRunPlusTestNormal
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        # 在导入预览页面中显示跳过的记录

        import_id_fields = ('id',)
        # 对象标识的默认字段是id，您可以选择在导入时设置哪些字段用作id

        fields = (
            'ItemScore',
            'malefirst',
            'maleSecond',
            'femalefirst',
            'femaleSecond',
        )

class OneMinuteSitupsAndPullUpPlusNormalResource(resources.ModelResource):
    def __init__(self):
        super(OneMinuteSitupsAndPullUpPlusNormalResource, self).__init__()
        field_list = apps.get_model('app', 'FiftymeterTestNormal')._meta.fields
        self.verbose_name_dict = {}
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name
        print(self.verbose_name_dict)

    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            # print(field_name)
            if field_name in self.verbose_name_dict.keys():
                field.colum_name = self.verbose_name_dict[field_name]
        return fields

    class Meta:
        model = OneMinuteSitupsAndPullUpPlusNormal
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        # 在导入预览页面中显示跳过的记录

        import_id_fields = ('id',)
        # 对象标识的默认字段是id，您可以选择在导入时设置哪些字段用作id

        fields = (
            'ItemScore',
            'malefirst',
            'maleSecond',
            'femalefirst',
            'femaleSecond',
        )


class TecherInfoResource(resources.ModelResource):
    def __init__(self):
        super(TecherInfoResource, self).__init__()
        field_list = apps.get_model('app', 'TecherInfo')._meta.fields
        self.verbose_name_dict = {}
        for i in field_list:
            self.verbose_name_dict[i.name] = i.verbose_name
        print(self.verbose_name_dict)

    def get_export_fields(self):
        fields = self.get_fields()
        for field in fields:
            field_name = self.get_field_name(field)
            # print(field_name)
            if field_name in self.verbose_name_dict.keys():
                field.colum_name = self.verbose_name_dict[field_name]
        return fields

    class Meta:
        model = TecherInfo
        skip_unchanged = True
        # 导入数据时，如果该条数据未修改过，则会忽略
        report_skipped = True
        # 在导入预览页面中显示跳过的记录

        import_id_fields = ('id',)
        # 对象标识的默认字段是id，您可以选择在导入时设置哪些字段用作id

        fields = (
            'techerName',
            'techerGender',
            'mobileNo',
            'officeNo',
            'office',
        )
        # 白名单

        # exclude = (
        #     'create_time',
        #     'update_time',
        # )
        # 黑名单


class StudentsAdmin(object):
    list_display = [

        'gradeclass',
        'classname',
        'address',
        'studentid',
        'name',
        'gender',
        'bithday',
        'idcardno',
        'stature',
        'weight',
        'lungcapacity',
        'fiftymeter',
        'middle_distancerun',
        'sitandreach',
        'standingbroadjump',
        'pull_ups',
        'Oneminutesitups',
        'score',
        'enrollment',
        'remarks',
    ]
    ordering = ['id']
    # 按照id顺序排列，如果是倒序-id
    search_fields = ['gradeclass', 'classname', 'address', 'studentid', 'name', 'gender', 'bithday', 'idcardno', ]
    # 要搜索的字段
    list_filter = ['gradeclass', 'classname', 'address', 'studentid', 'name', 'gender', 'bithday', 'idcardno',
                   'enrollment']
    # 要筛选的字段
    show_detail_fields = ['class_name']
    # 要展示详情的字段
    list_editable = [
        'gradeclass',
        'classname',
        'address',
        'studentid',
        'name',
        'gender',
        'bithday',
        'idcardno',
        'stature',
        'weight',
        'lungcapacity',
        'fiftymeter',
        'middle_distancerun',
        'sitandreach',
        'standingbroadjump',
        'pull_ups',
        'Oneminutesitups',
        'score',
        'enrollment',
        'remarks',
    ]
    # 列表可直接修改的字段
    list_per_page = 60
    # 分页
    import_export_args = {
        'import_resource_class': StudentsInfoResource,
        # 'export_resource_class': ProductInfoResource,
    }
    # 配置导入按钮


class ClassAdmin(object):
    list_display = [ 'class_name', ]
    ordering = ['id']
    # 按照id顺序排列，如果是倒序-id
    search_fields = ['class_name']
    # 要搜索的字段
    list_filter = ['class_name']
    # 要筛选的字段
    show_detail_fields = ['class_name']
    # 要展示详情的字段
    list_editable = ['class_name']
    # 列表可直接修改的字段
    list_per_page = 30
    # 分页
    import_export_args = {
        'import_resource_class': ClassInfoResource,
        # 'export_resource_class': ProductInfoResource,
    }
    # 配置导入按钮

class ItemWeightAdmin(object):
    ordering = ['id']
    list_display = ['BMI', 'lungcapacity', 'fiftymeter','sitandreach', 'standingbroadjump','pull_ups', 'Oneminutesitups','middle_distancerun',]
    list_editable =['BMI', 'lungcapacity', 'fiftymeter','sitandreach', 'standingbroadjump','pull_ups', 'Oneminutesitups','middle_distancerun',]

class BMITestNormalsAdmin(object):
    ordering = ['id']
    list_display = [ 'classtype', 'ItemScore', 'male','female',]
    list_editable =['classtype', 'ItemScore', 'male','female',]

class LungCapacityTestNormalAdmin(object):
    ordering = ['id']
    list_display = ['classtype', 'ItemScore', 'malefirst','maleSecond','femalefirst','femaleSecond',]
    list_editable =['classtype', 'ItemScore', 'malefirst','maleSecond','femalefirst','femaleSecond',]
    import_export_args = {
        'import_resource_class': LungCapacityTestNormalResource,
        # 'export_resource_class': ProductInfoResource,
    }


class FiftymeterTestNormalAdmin(object):
    ordering = ['id']
    list_display = ['classtype', 'ItemScore', 'malefirst','maleSecond','femalefirst','femaleSecond',]
    list_editable =['classtype', 'ItemScore', 'malefirst','maleSecond','femalefirst','femaleSecond',]
    import_export_args = {
        'import_resource_class': FiftymeterTestNormalResource,
        # 'export_resource_class': ProductInfoResource,
    }

class SitandReachTestNoramlAdmin(object):
    ordering = ['id']
    list_display = [ 'classtype', 'ItemScore', 'malefirst','maleSecond','femalefirst','femaleSecond',]
    list_editable =['classtype', 'ItemScore', 'malefirst','maleSecond','femalefirst','femaleSecond',]
    import_export_args = {
        'import_resource_class': SitandReachTestNoramlResource,
        # 'export_resource_class': ProductInfoResource,
    }


class StandingBroadJumpTestNormalAdmin(object):
    ordering = ['id']
    list_display = ['classtype', 'ItemScore', 'malefirst','maleSecond','femalefirst','femaleSecond',]
    list_editable =['classtype', 'ItemScore', 'malefirst','maleSecond','femalefirst','femaleSecond',]
    import_export_args = {
        'import_resource_class': StandingBroadJumpTestNormalResource,
        # 'export_resource_class': ProductInfoResource,
    }


class OneMinuteSitupsAndPullUpTestNormalAdmin(object):
    ordering = ['id']
    list_display = [ 'classtype', 'ItemScore', 'malefirst','maleSecond','femalefirst','femaleSecond',]
    list_editable =['classtype', 'ItemScore', 'malefirst','maleSecond','femalefirst','femaleSecond',]
    import_export_args = {
        'import_resource_class': OneMinuteSitupsAndPullUpTestNormalResource,
        # 'export_resource_class': ProductInfoResource,
    }


class MiddleDistanceRunTestNormalAdmin(object):
    ordering = ['id']
    list_display = ['classtype', 'ItemScore', 'malefirst','maleSecond','femalefirst','femaleSecond',]
    list_editable =['classtype', 'ItemScore', 'malefirst','maleSecond','femalefirst','femaleSecond',]
    import_export_args = {
        'import_resource_class': MiddleDistanceRunTestNormalResource,
        # 'export_resource_class': ProductInfoResource,
    }


class MiddleDistanceRunPlusTestNormalAdmin(object):
    ordering = ['id']
    list_display = [ 'ItemScore', 'malefirst','maleSecond','femalefirst','femaleSecond',]
    list_editable =[ 'ItemScore', 'malefirst','maleSecond','femalefirst','femaleSecond',]
    import_export_args = {
        'import_resource_class': MiddleDistanceRunPlusTestNormalResource,
        # 'export_resource_class': ProductInfoResource,
    }


class OneMinuteSitupsAndPullUpPlusNormalAdmin(object):
    ordering = ['id']
    list_display = ['id',  'ItemScore', 'malefirst','maleSecond','femalefirst','femaleSecond',]
    list_editable =['ItemScore', 'malefirst','maleSecond','femalefirst','femaleSecond',]
    import_export_args = {
        'import_resource_class': OneMinuteSitupsAndPullUpPlusNormalResource,
        # 'export_resource_class': ProductInfoResource,
    }


class TestSiteAmdin(object):
    list_display = [ 'siteName', ]


class TestDatetimeAdmin(object):
    list_display = [ 'testTime', ]


class TecherInfoAdmin(object):
    list_display = [ 'techerName', 'techerGender', 'mobileNo', 'officeNo', 'office']
    ordering = ['id']
    # 按照id顺序排列，如果是倒序-id
    search_fields = ['techerName', 'mobileNo']
    # 要搜索的字段
    list_filter = ['techerName', 'mobileNo']
    # 要筛选的字段
    show_detail_fields = ['techerName']
    # 要展示详情的字段
    list_editable = ['techerName', 'techerGender', 'mobileNo', 'officeNo', 'office']
    # 列表可直接修改的字段
    list_per_page = 40
    # 分页
    import_export_args = {
        'import_resource_class': TecherInfoResource,
        # 'export_resource_class': ProductInfoResource,
    }


class TestScheduleAdmin(object):
    list_display = ['testtecher', 'testsite', 'testdatetime', 'testClass', ]


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
    # 开启主题自由切换


class GlobalSetting(object):
    global_search_models = [Class]
    # 配置全局搜索选项，默认搜索组、用户、日志记录
    site_title = "体能测试成绩上报辅助系统"
    # 标题
    site_footer = "蚌埠学院"
    # 页脚

    # menu_style = "accordion"
    # 左侧菜单收缩功能
    apps_icons = {
        "app": "fa fa-music",
    }
    # 配置应用图标，即一级菜单图标
    global_models_icon = {
        Class: "fa fa-film",
    }
    # 配置模型图标，即二级菜单图标


xadmin.site.register(Students, StudentsAdmin)
xadmin.site.register(Class, ClassAdmin)
xadmin.site.register(TestSite, TestSiteAmdin)
xadmin.site.register(TestDatetime, TestDatetimeAdmin)
xadmin.site.register(TecherInfo, TecherInfoAdmin)
xadmin.site.register(TestSchedule, TestScheduleAdmin)

xadmin.site.register(ItemWeight,ItemWeightAdmin)
xadmin.site.register(BMITestNormals,BMITestNormalsAdmin)
xadmin.site.register(LungCapacityTestNormal,LungCapacityTestNormalAdmin)
xadmin.site.register(FiftymeterTestNormal,FiftymeterTestNormalAdmin)
xadmin.site.register(SitandReachTestNoraml,SitandReachTestNoramlAdmin)
xadmin.site.register(StandingBroadJumpTestNormal,StandingBroadJumpTestNormalAdmin)
xadmin.site.register(OneMinuteSitupsAndPullUpTestNormal,OneMinuteSitupsAndPullUpTestNormalAdmin)
xadmin.site.register(MiddleDistanceRunTestNormal,MiddleDistanceRunTestNormalAdmin)
xadmin.site.register(OneMinuteSitupsAndPullUpPlusNormal,OneMinuteSitupsAndPullUpPlusNormalAdmin)
xadmin.site.register(MiddleDistanceRunPlusTestNormal,MiddleDistanceRunPlusTestNormalAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(LoginView, LoginViewAdmin)
xadmin.site.register(LogoutView, LogOutViewAdmin)
