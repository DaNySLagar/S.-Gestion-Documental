# Generated by Django 4.2 on 2023-05-15 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0010_alter_libro_destino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='destino',
            field=models.CharField(choices=[('opcion1', 'Opción 1'), ('opcion2', 'Opción 2'), ('opcion3', 'Opción 3')], max_length=100, null=True),
        ),
    ]
