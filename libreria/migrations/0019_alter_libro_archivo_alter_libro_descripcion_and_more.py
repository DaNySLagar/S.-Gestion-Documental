# Generated by Django 4.2 on 2023-05-22 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0018_libro2_marcado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='archivo',
            field=models.FileField(null=True, upload_to='imagenes/', verbose_name='Archivo'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='descripcion',
            field=models.TextField(null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='destino',
            field=models.CharField(max_length=100, null=True, verbose_name='Oficina de destino'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='f_emision',
            field=models.DateField(null=True, verbose_name='Fecha de emisión'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='f_envio',
            field=models.DateField(null=True, verbose_name='Fecha de envío'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='oficio',
            field=models.TextField(null=True, verbose_name='Nro. de Oficio'),
        ),
        migrations.AlterField(
            model_name='libro2',
            name='archivo',
            field=models.FileField(null=True, upload_to='imagenes/', verbose_name='Archivo'),
        ),
        migrations.AlterField(
            model_name='libro2',
            name='descripcion',
            field=models.TextField(null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='libro2',
            name='oficio',
            field=models.TextField(null=True, verbose_name='Nro. de Oficio'),
        ),
    ]
