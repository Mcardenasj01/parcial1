# Generated by Django 3.2.16 on 2024-03-19 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productoControl', '0002_auto_20240318_2355'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductoControlPlaga',
            new_name='Plaga',
        ),
        migrations.RenameField(
            model_name='plaga',
            old_name='carencia_producto_control_plaga',
            new_name='carencia_plaga',
        ),
    ]