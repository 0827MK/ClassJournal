# Generated by Django 3.2.8 on 2023-01-22 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_department_employee'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Department',
            new_name='クラス',
        ),
        migrations.RenameModel(
            old_name='Employee',
            new_name='今日の記録',
        ),
    ]
