# Generated by Django 4.2 on 2023-05-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0006_remove_libro_titulo_libro_destino_libro_f_emision_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='archivo',
            field=models.FileField(null=True, upload_to='imagenes/', verbose_name='Imagen'),
        ),
    ]
