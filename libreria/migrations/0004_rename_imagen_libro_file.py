# Generated by Django 4.2 on 2023-05-11 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_alter_libro_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='imagen',
            new_name='file',
        ),
    ]
