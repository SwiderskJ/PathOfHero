# Generated by Django 4.1.7 on 2023-03-27 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercurrency',
            name='diamonds',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='usercurrency',
            name='gold',
            field=models.IntegerField(default=100),
        ),
    ]
