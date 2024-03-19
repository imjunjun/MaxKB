# Generated by Django 4.1.10 on 2024-03-19 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemSetting',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('type', models.IntegerField(choices=[('0', '邮箱')], default='0', max_length=5, primary_key=True, serialize=False, verbose_name='设置类型')),
                ('meta', models.JSONField(default=dict, verbose_name='配置数据')),
            ],
            options={
                'db_table': 'system_setting',
            },
        ),
    ]
