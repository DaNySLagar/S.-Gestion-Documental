# Generated by Django 4.2 on 2023-05-30 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0034_alter_libro6_apellido_materno_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro6',
            name='apellido_paterno',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Apellido Paterno'),
        ),
        migrations.AlterField(
            model_name='libro6',
            name='nombres',
            field=models.CharField(max_length=50, null=True, verbose_name='Nombres'),
        ),
    ]
