# Generated by Django 3.2.13 on 2022-11-20 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20221120_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='point',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='회원등급',
            field=models.TextField(blank=True, default='i3', null=True),
        ),
    ]