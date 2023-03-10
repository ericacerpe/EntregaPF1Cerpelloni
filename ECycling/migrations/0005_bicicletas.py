# Generated by Django 3.2.16 on 2023-01-10 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ECycling', '0004_auto_20230108_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='bicicletas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=60)),
                ('rodado', models.IntegerField(default=0)),
                ('marca', models.CharField(max_length=50, null=True)),
                ('precio', models.FloatField(default=0)),
            ],
        ),
    ]
