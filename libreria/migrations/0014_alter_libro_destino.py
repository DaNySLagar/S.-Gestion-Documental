# Generated by Django 4.2 on 2023-05-15 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0013_alter_libro_destino'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='destino',
            field=models.CharField(max_length=100, null=True, verbose_name='Destino'),
        ),
    ]
