# Generated by Django 4.0.1 on 2022-01-21 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_insert_creat_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insert',
            name='creat_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
