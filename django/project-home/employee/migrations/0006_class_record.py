# Generated by Django 3.2.8 on 2023-01-22 18:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0005_auto_20230123_0307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='クラス名')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now, verbose_name='日付:')),
                ('name', models.CharField(max_length=20, verbose_name='記録者:')),
                ('event', models.CharField(blank=True, max_length=50, null=True, verbose_name='学校行事・連絡事項:')),
                ('weather', models.CharField(max_length=10, verbose_name='天気:')),
                ('subject1', models.CharField(blank=True, max_length=10, null=True, verbose_name='1校時:科目:')),
                ('substance1', models.CharField(blank=True, max_length=30, null=True, verbose_name='↑内容↑:')),
                ('subject2', models.CharField(blank=True, max_length=10, null=True, verbose_name='2校時:科目:')),
                ('substance2', models.CharField(blank=True, max_length=30, null=True, verbose_name='↑内容↑:')),
                ('subject3', models.CharField(blank=True, max_length=10, null=True, verbose_name='3校時:科目:')),
                ('substance3', models.CharField(blank=True, max_length=30, null=True, verbose_name='↑内容↑:')),
                ('subject4', models.CharField(blank=True, max_length=10, null=True, verbose_name='4校時:科目:')),
                ('substance4', models.CharField(blank=True, max_length=30, null=True, verbose_name='↑内容↑:')),
                ('cleaning1', models.CharField(blank=True, max_length=30, null=True, verbose_name='教室掃除:')),
                ('cleaning2', models.CharField(blank=True, max_length=30, null=True, verbose_name='特別区域掃除:')),
                ('feel', models.TextField(verbose_name='所感:')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employee.class', verbose_name='クラス:')),
            ],
        ),
    ]
