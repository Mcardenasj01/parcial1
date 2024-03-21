# Generated by Django 3.2.16 on 2024-03-19 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_catrastro', models.CharField(max_length=20, unique=True)),
                ('municipio', models.CharField(max_length=15)),
                ('propietario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productor.productor')),
            ],
            options={
                'verbose_name': 'Finca',
                'verbose_name_plural': 'Fincas',
            },
        ),
    ]
