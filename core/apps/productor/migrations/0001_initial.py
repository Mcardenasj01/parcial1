# Generated by Django 3.2.16 on 2024-03-19 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=10, unique=True)),
                ('primer_nombre', models.CharField(max_length=15)),
                ('segundo_nombre', models.CharField(blank=True, max_length=15, null=True)),
                ('primer_apellido', models.CharField(max_length=15)),
                ('segundo_apellido', models.CharField(blank=True, max_length=15, null=True)),
                ('telefono', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Productor',
                'verbose_name_plural': 'Productores',
            },
        ),
    ]
