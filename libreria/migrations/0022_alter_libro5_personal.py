# Generated by Django 4.2 on 2023-05-25 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0021_libro3_libro4_libro5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro5',
            name='personal',
            field=models.CharField(max_length=100, null=True, verbose_name='Personal'),
        ),
    ]
