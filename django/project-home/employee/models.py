from django.db import models
from django.utils import timezone

class Class(models.Model):
    name = models.CharField('クラス名', max_length=20)
    def __str__(self):
        return self.name

class Record(models.Model):
    #ほかのモデルと紐づける
    department = models.ForeignKey(
        Class, verbose_name='クラス:', on_delete=models.PROTECT,
    )
    created_at = models.DateField('日付:', default=timezone.now)
    person = models.CharField('記録者:', max_length=20, blank=False, null=False)
    event = models.CharField('学校行事・連絡事項:', max_length=50, blank=True, null=True)
    weather = models.CharField('天気:', max_length=10, blank=False, null=False)
    subject1 = models.CharField('1校時:科目:',max_length=10, blank=True, null=True)
    substance1 = models.CharField('↑内容↑:',max_length=30, blank=True, null=True)
    subject2 = models.CharField('2校時:科目:',max_length=10, blank=True, null=True)
    substance2 = models.CharField('↑内容↑:',max_length=30, blank=True, null=True)
    subject3 = models.CharField('3校時:科目:',max_length=10, blank=True, null=True)
    substance3 = models.CharField('↑内容↑:',max_length=30, blank=True, null=True)
    subject4 = models.CharField('4校時:科目:',max_length=10, blank=True, null=True)
    substance4 = models.CharField('↑内容↑:',max_length=30, blank=True, null=True)
    cleaning1 = models.CharField('教室掃除:',max_length=30, blank=True, null=True)
    cleaning2 = models.CharField('特別区域掃除:',max_length=30, blank=True, null=True)
    feel = models.TextField('所感:', blank=False, null=False)
    teacher = models.TextField('先生から:', blank=True, null=True)
    def __str__(self):
        return '{0} {1}'.format(self.department, self.person)