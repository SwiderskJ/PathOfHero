# Generated by Django 4.1.6 on 2023-02-09 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='maze',
            name='slug',
            field=models.CharField(default=None, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]