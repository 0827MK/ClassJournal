# Generated by Django 3.2.8 on 2023-01-27 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_record_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='teacher',
            field=models.TextField(blank=True, null=True, verbose_name='先生から:'),
        ),
    ]
