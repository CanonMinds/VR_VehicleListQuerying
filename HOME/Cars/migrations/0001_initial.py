# Generated by Django 2.1.5 on 2020-05-23 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Red Car', 'RedCar'), ('Blue Car', 'BlueCar'), ('Green Car', 'Green Car')], default='Red Car', max_length=200)),
            ],
        ),
    ]
