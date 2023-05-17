# Generated by Django 4.2.1 on 2023-05-14 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_announcement_status_ad_user_status_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='convenient_time',
            field=models.CharField(max_length=50, verbose_name='Когда удобно принимать звонки'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(default='Пользователь', max_length=50, verbose_name='Роль'),
        ),
    ]
