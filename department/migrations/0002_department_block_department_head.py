# Generated by Django 4.1 on 2022-09-08 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='block',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='department',
            name='head',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
