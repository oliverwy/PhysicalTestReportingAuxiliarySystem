from django.db import models
import computed_property


class ItemWeight(models.Model):
    id = models.BigAutoField(verbose_name="序号", primary_key=True)
    BMI = models.FloatField(verbose_name="体重指数BMI", default=0)
    lungcapacity = models.FloatField(verbose_name="肺活量", default=0)
    fiftymeter = models.FloatField(verbose_name="50米跑", default=0)
    sitandreach = models.FloatField(verbose_name="坐位体前屈", default=0)
    standingbroadjump = models.FloatField(verbose_name="立定跳远", default=0)
    pull_ups = models.FloatField(verbose_name="引体向上", default=0)
    Oneminutesitups = models.FloatField(verbose_name="一分钟仰卧起坐", default=0)
    middle_distancerun = models.FloatField(verbose_name="中长跑", default=0)

    class Meta:
        verbose_name = "单项指标与权重"
        verbose_name_plural = "单项指标与权重"

    def __str__(self):
        return "单项指标与权重"


class BMITestNormals(models.Model):
    id = models.AutoField(verbose_name="序号", primary_key=True)
    classtype = models.CharField(verbose_name="等级", max_length=10, default=0)
    ItemScore = models.IntegerField(verbose_name="单项分值", default=0)
    male = models.FloatField(verbose_name="BMI男范围", default="0.0")
    female = models.FloatField(verbose_name="BMI女范围",  default='0.0')

    class Meta:
        verbose_name = "体重指数（BMI）单项评分表"
        verbose_name_plural = "体重指数（BMI）单项评分表"


class LungCapacityTestNormal(models.Model):
    id = models.AutoField(verbose_name="序号", primary_key=True)
    classtype = models.CharField(verbose_name="等级", max_length=10, default=0)
    ItemScore = models.IntegerField(verbose_name="单项分值", default=0)
    malefirst = models.IntegerField(verbose_name="大一大二指标男", default=0)
    maleSecond = models.IntegerField(verbose_name="大三大四指标男", default=0)
    femalefirst = models.IntegerField(verbose_name="大一大二指标女", default=0)
    femaleSecond = models.IntegerField(verbose_name="大三大四指标女", default=0)

    class Meta:
        verbose_name = "肺活量单项评分表（单位：毫升）"
        verbose_name_plural = "肺活量单项评分表（单位：毫升）"


class FiftymeterTestNormal(models.Model):
    id = models.AutoField(verbose_name="序号", primary_key=True)
    classtype = models.CharField(verbose_name="等级", max_length=10, default=0)
    ItemScore = models.IntegerField(verbose_name="单项分值", default=0)
    malefirst = models.FloatField(verbose_name="大一大二指标男", default=0)
    maleSecond = models.FloatField(verbose_name="大三大四指标男", default=0)
    femalefirst = models.FloatField(verbose_name="大一大二指标女", default=0)
    femaleSecond = models.FloatField(verbose_name="大三大四指标女", default=0)

    class Meta:
        verbose_name = "50米跑单项评分表（单位：秒）"
        verbose_name_plural = "50米跑单项评分表（单位：秒）"


class SitandReachTestNoraml(models.Model):
    id = models.AutoField(verbose_name="序号", primary_key=True)
    classtype = models.CharField(verbose_name="等级", max_length=10, default=0)
    ItemScore = models.IntegerField(verbose_name="单项分值", default=0)
    malefirst = models.FloatField(verbose_name="大一大二指标男", default=0)
    maleSecond = models.FloatField(verbose_name="大三大四指标男", default=0)
    femalefirst = models.FloatField(verbose_name="大一大二指标女", default=0)
    femaleSecond = models.FloatField(verbose_name="大三大四指标女", default=0)

    class Meta:
        verbose_name = "坐位体前屈单项评分表（单位：厘米）"
        verbose_name_plural = "坐位体前屈单项评分表（单位：厘米）"


class StandingBroadJumpTestNormal(models.Model):
    id = models.AutoField(verbose_name="序号", primary_key=True)
    classtype = models.CharField(verbose_name="等级", max_length=10, default=0)
    ItemScore = models.IntegerField(verbose_name="单项分值", default=0)
    malefirst = models.FloatField(verbose_name="大一大二指标男", default=0)
    maleSecond = models.FloatField(verbose_name="大三大四指标男", default=0)
    femalefirst = models.FloatField(verbose_name="大一大二指标女", default=0)
    femaleSecond = models.FloatField(verbose_name="大三大四指标女", default=0)

    class Meta:
        verbose_name = "立定跳远单项评分表（单位：厘米）"
        verbose_name_plural = "立定跳远单项评分表（单位：厘米）"


class OneMinuteSitupsAndPullUpTestNormal(models.Model):
    id = models.AutoField(verbose_name="序号", primary_key=True)
    classtype = models.CharField(verbose_name="等级", max_length=10, default=0)
    ItemScore = models.IntegerField(verbose_name="单项分值", default=0)
    malefirst = models.IntegerField(verbose_name="大一大二指标男", default=0)
    maleSecond = models.IntegerField(verbose_name="大三大四指标男", default=0)
    femalefirst = models.IntegerField(verbose_name="大一大二指标女", default=0)
    femaleSecond = models.IntegerField(verbose_name="大三大四指标女", default=0)

    class Meta:
        verbose_name = "男生引体向上、女生一分钟仰卧起坐评分表（单位：次）"
        verbose_name_plural = "男生引体向上、女生一分钟仰卧起坐评分表（单位：次）"


class MiddleDistanceRunTestNormal(models.Model):
    id = models.AutoField(verbose_name="序号", primary_key=True)
    classtype = models.CharField(verbose_name="等级", max_length=10, default=0)
    ItemScore = models.IntegerField(verbose_name="单项分值", default=0)
    malefirst = models.FloatField(verbose_name="大一大二指标男", default=0)
    maleSecond = models.FloatField(verbose_name="大三大四指标男", default=0)
    femalefirst = models.FloatField(verbose_name="大一大二指标女", default=0)
    femaleSecond = models.FloatField(verbose_name="大三大四指标女", default=0)

    class Meta:
        verbose_name = "男生1000米、女生800米耐力跑单项评分表（单位：分·秒）"
        verbose_name_plural = "男生1000米、女生800米耐力跑单项评分表（单位：分·秒）"


class MiddleDistanceRunPlusTestNormal(models.Model):
    id = models.AutoField(verbose_name="序号", primary_key=True)
    ItemScore = models.IntegerField(verbose_name="单项加分值", default=0)
    malefirst = models.CharField(verbose_name="大一大二指标男", max_length=10, default=0)
    maleSecond = models.CharField(verbose_name="大三大四指标男", max_length=10, default=0)
    femalefirst = models.CharField(verbose_name="大一大二指标女", max_length=10, default=0)
    femaleSecond = models.CharField(verbose_name="大三大四指标女", max_length=10, default=0)

    class Meta:
        verbose_name = "男生1000米跑、女生800米加分表（单位：分·秒）"
        verbose_name_plural = "男生1000米跑、女生800米加分表（单位：分·秒）"


class OneMinuteSitupsAndPullUpPlusNormal(models.Model):
    id = models.AutoField(verbose_name="序号", primary_key=True)
    ItemScore = models.IntegerField(verbose_name="单项加分值", default=0)
    malefirst = models.IntegerField(verbose_name="大一大二指标男", default=0)
    maleSecond = models.IntegerField(verbose_name="大三大四指标男", default=0)
    femalefirst = models.IntegerField(verbose_name="大一大二指标女", default=0)
    femaleSecond = models.IntegerField(verbose_name="大三大四指标女", default=0)

    class Meta:
        verbose_name = "男生引体向上、女生仰卧起坐加分表（单位：次）"
        verbose_name_plural = "男生引体向上、女生仰卧起坐加分表（单位：次）"


class Class(models.Model):
    id = models.AutoField(verbose_name="序号", primary_key=True)
    class_name = models.CharField(verbose_name='专业班级', max_length=100)

    class Meta:
        verbose_name = '专业班级表'
        verbose_name_plural = '专业班级表'

    def __str__(self):
        return self.class_name


class TestSite(models.Model):
    id = models.AutoField(verbose_name="序号", primary_key=True)
    siteName = models.CharField(verbose_name="测试场地", max_length=100)

    class Meta:
        verbose_name = "测试场地"
        verbose_name_plural = "测试场地"

    def __str__(self):
        return self.siteName


class TestDatetime(models.Model):
    id = models.AutoField(verbose_name="序号", primary_key=True)
    testTime = models.CharField(verbose_name="测试时间", max_length=100)

    class Meta:
        verbose_name = "测试时间"
        verbose_name_plural = "测试时间"

    def __str__(self):
        return self.testTime


class TecherInfo(models.Model):
    SEX = (('男', '男'), ('女', '女'))
    id = models.AutoField(verbose_name="序号", primary_key=True)
    techerName = models.CharField(verbose_name="教师姓名", max_length=20)
    techerGender = models.CharField(choices=SEX, verbose_name='性别', max_length=10)
    mobileNo = models.CharField(verbose_name="手机号码", max_length=20)
    officeNo = models.CharField(verbose_name="座机号码", max_length=20, blank=True)
    office = models.CharField(verbose_name="办公室", max_length=50, blank=True)

    class Meta:
        verbose_name = "教师信息表"
        verbose_name_plural = "教师信息表"

    def __str__(self):
        return self.techerName


class TestSchedule(models.Model):
    id = models.AutoField(verbose_name="序号", primary_key=True)
    testtecher = models.ForeignKey(TecherInfo, verbose_name='测试教师', on_delete=models.CASCADE, blank=True, null=True)
    testsite = models.ForeignKey(TestSite, verbose_name='测试场地', on_delete=models.CASCADE, blank=True, null=True)
    testdatetime = models.ForeignKey(TestDatetime, verbose_name='测试时间', on_delete=models.CASCADE, blank=True, null=True)
    testClass = models.ForeignKey(Class, verbose_name='测试时间', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "测试时间场地安排表"
        verbose_name_plural = "测试时间场地安排表"


# Create your models here.
class Students(models.Model):
    SEX = (('男', '男'), ('女', '女'))
    # testtecher=models.CharField(verbose_name="测试教师",max_length=50,blank=True)
    # testsite = models.CharField(verbose_name="测试场地", max_length=50, blank=True)
    # testdatetime = models.CharField(verbose_name="测试时间", max_length=50, blank=True)
    id = models.AutoField(verbose_name="序号", primary_key=True)
    gradeclass = models.CharField(verbose_name="年级", max_length=20)
    classname = models.CharField(verbose_name="专业班级", max_length=50)
    address = models.CharField(verbose_name='家庭住址', max_length=250, blank=True)
    studentid = models.CharField(verbose_name="学号", max_length=18)
    nationality = models.CharField(verbose_name="民族", max_length=50, blank=True)
    name = models.CharField(verbose_name='学生姓名', max_length=50)
    gender = models.CharField(choices=SEX, verbose_name='性别', max_length=10)
    bithday = computed_property.ComputedCharField(verbose_name="出生日期", compute_from='computer_bithday', max_length=30,
                                                  null=True)
    idcardno = models.CharField(verbose_name="身份证号", max_length=20)
    stature = models.FloatField(verbose_name="身高", default=0)
    weight = models.FloatField(verbose_name="体重", default=0)
    lungcapacity = models.IntegerField(verbose_name="肺活量", default=0)
    middle_distancerun = models.FloatField(verbose_name="中长跑", default=0)
    fiftymeter = models.FloatField(verbose_name="50米", default=0)
    standingbroadjump = models.FloatField(verbose_name="立定跳远", default=0)
    pull_ups = models.IntegerField(verbose_name="引体向上", default=0)
    sitandreach = models.FloatField(verbose_name="坐位体前屈", default=0)
    Oneminutesitups = models.IntegerField(verbose_name="一分钟仰卧起坐", default=0)
    score = computed_property.ComputedFloatField(verbose_name='分数',
                                                 compute_from='caculate_it')  # models.FloatField(verbose_name="总分", default=0)
    enrollment = models.CharField(verbose_name='入学时间', max_length=50, blank=True, null=True)
    remarks = models.TextField(verbose_name='备注', blank=True)

    @property
    def computer_bithday(self):
        return self.idcardno[6:10] + "-" + self.idcardno[11:12] + "-" + self.idcardno[13:14]

    @property
    def caculate_it(self):
        # print(self.stature)
        # print(self.weight)
        bmi = self.caculate_bmi(self.gender,self.weight, self.stature)
        fl = self.caculate_lungcapacity(self.lungcapacity,self.gender,self.gradeclass)
        fifty=self.caculate_fiftymeter(self.gradeclass,self.gender,self.fiftymeter)
        stbroadjump=self.caculate_standingbroadjump(self.gradeclass,self.gender,self.standingbroadjump)
        sitareach=self.caculate_sitandreach(self.gradeclass,self.gender,self.sitandreach)
        m=self.caculate_middle_distancerun(self.gradeclass,self.gender,self.middle_distancerun)
        one=self.caculate_Oneminutesitups(self.gradeclass,self.gender,self.Oneminutesitups)
        pullsup=self.caculate_pull_ups(self.gradeclass,self.gender,self.pull_ups)
        x=ItemWeight.objects.all().first()
        score=bmi*x.BMI+fl*x.lungcapacity+fifty*x.fiftymeter+stbroadjump*x.standingbroadjump+sitareach*x.sitandreach+m*x.middle_distancerun
        if self.gender=='女':
            score=score+one*x.pull_ups
        else:
            score=score+pullsup*x.Oneminutesitups
        return round(score,1);


    def caculate_bmi(self, lgender,x, y):
        if y>0:
            nc=round((x / (y * y)) * 10000,2)
            if (lgender == '男'):
                x=BMITestNormals.objects.filter(male__lte=nc).order_by('-male').first().ItemScore
            else:
                x = BMITestNormals.objects.filter(female__lte=nc).order_by('-male').first().ItemScore
        return x

    def caculate_lungcapacity(self, lc,lgender,lgradeclass):
        if (lgender=='男'):
            if (lgradeclass=="大一" or lgradeclass=="大二"):
                x = LungCapacityTestNormal.objects.filter(malefirst__lte=lc).order_by('-ItemScore').first().ItemScore
            else:
                x = LungCapacityTestNormal.objects.filter(maleSecond__lte=lc).order_by('-ItemScore').first().ItemScore
        else:
            if (lgradeclass=="大一" or lgradeclass=="大二"):
                x = LungCapacityTestNormal.objects.filter(femalefirst__lte=lc).order_by('-ItemScore').first().ItemScore
            else:
                x = LungCapacityTestNormal.objects.filter(femaleSecond__lte=lc).order_by('-ItemScore').first().ItemScore

        return x

    def caculate_fiftymeter(self,lgradeclass,lgender,lc):
        if (lgender=='男'):
            if (lgradeclass=="大一" or lgradeclass=="大二"):
                x = FiftymeterTestNormal.objects.filter(malefirst__gte=lc).order_by('-ItemScore').first().ItemScore
            else:
                x = FiftymeterTestNormal.objects.filter(maleSecond__gte=lc).order_by('-ItemScore').first().ItemScore
        else:
            if (lgradeclass=="大一" or lgradeclass=="大二"):
                x = FiftymeterTestNormal.objects.filter(femalefirst__gte=lc).order_by('-ItemScore').first().ItemScore
            else:
                x = FiftymeterTestNormal.objects.filter(femaleSecond__gte=lc).order_by('-ItemScore').first().ItemScore
        return x

    def caculate_standingbroadjump(self,lgradeclass,lgender,lc):
        if (lgender=='男'):
            if (lgradeclass=="大一" or lgradeclass=="大二"):
                x = StandingBroadJumpTestNormal.objects.filter(malefirst__lte=lc).order_by('-ItemScore').first().ItemScore
            else:
                x = StandingBroadJumpTestNormal.objects.filter(maleSecond__lte=lc).order_by('-ItemScore').first().ItemScore
        else:
            if (lgradeclass=="大一" or lgradeclass=="大二"):
                x = StandingBroadJumpTestNormal.objects.filter(femalefirst__lte=lc).order_by('-ItemScore').first().ItemScore
            else:
                x = StandingBroadJumpTestNormal.objects.filter(femaleSecond__lte=lc).order_by('-ItemScore').first().ItemScore
        return x

    def caculate_sitandreach(self,lgradeclass,lgender,lc):
        if (lgender=='男'):
            if (lgradeclass=="大一" or lgradeclass=="大二"):
                x = SitandReachTestNoraml.objects.filter(malefirst__lte=lc).order_by('-ItemScore').first().ItemScore
            else:
                x = SitandReachTestNoraml.objects.filter(maleSecond__lte=lc).order_by('-ItemScore').first().ItemScore
        else:
            if (lgradeclass=="大一" or lgradeclass=="大二"):
                x = SitandReachTestNoraml.objects.filter(femalefirst__lte=lc).order_by('-ItemScore').first().ItemScore
            else:
                x = SitandReachTestNoraml.objects.filter(femaleSecond__lte=lc).order_by('-ItemScore').first().ItemScore
        return x

    def caculate_middle_distancerun(self,lgradeclass,lgender,lc):
        if (lgender=='男'):
            if (lgradeclass=="大一" or lgradeclass=="大二"):
                x = MiddleDistanceRunTestNormal.objects.filter(malefirst__gte=lc).order_by('-ItemScore').first().ItemScore
            else:
                x = MiddleDistanceRunTestNormal.objects.filter(maleSecond__gte=lc).order_by('-ItemScore').first().ItemScore
        else:
            if (lgradeclass=="大一" or lgradeclass=="大二"):
                x = MiddleDistanceRunTestNormal.objects.filter(femalefirst__gte=lc).order_by('-ItemScore').first().ItemScore
            else:
                x = MiddleDistanceRunTestNormal.objects.filter(femaleSecond__gte=lc).order_by('-ItemScore').first().ItemScore
        return x

    def caculate_Oneminutesitups(self,lgradeclass,lgender,lc):
        if (lgender=='男'):
            x=0
        else:
            if (lgradeclass=="大一" or lgradeclass=="大二"):
                x = OneMinuteSitupsAndPullUpTestNormal.objects.filter(femalefirst__lte=lc).order_by('-femalefirst').first().ItemScore
            else:
                x = OneMinuteSitupsAndPullUpTestNormal.objects.filter(femaleSecond__lte=lc).order_by('-femaleSecond').first().ItemScore
        return x

    def caculate_pull_ups(self,lgradeclass,lgender,lc):
        if (lgender=='男'):
            if (lgradeclass=="大一" or lgradeclass=="大二"):
                x = OneMinuteSitupsAndPullUpTestNormal.objects.filter(malefirst__lte=lc).order_by('-malefirst').first().ItemScore
            else:
                x = OneMinuteSitupsAndPullUpTestNormal.objects.filter(maleSecond__lte=lc).order_by('-maleSecond').first().ItemScore
        else:
            x=0
        return x

    class Meta:
        verbose_name = "体能测试成绩表"
        verbose_name_plural = "体能测试成绩表"

    def __str__(self):
        return self.name + "-" + self.idcardno
