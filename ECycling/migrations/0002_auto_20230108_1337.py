# Generated by Django 3.2.16 on 2023-01-08 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ECycling', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='localidad',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='indumentaria',
            name='genero',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='indumentaria',
            name='nombre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='indumentaria',
            name='tipo',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='fecha',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
