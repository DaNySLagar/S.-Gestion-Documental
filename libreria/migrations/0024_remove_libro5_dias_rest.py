# Generated by Django 4.2 on 2023-05-26 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0023_libro6_remove_libro5_personal_libro5_libro6'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro5',
            name='dias_rest',
        ),
    ]
