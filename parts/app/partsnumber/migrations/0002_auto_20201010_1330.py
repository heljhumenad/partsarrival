# Generated by Django 2.2 on 2020-10-10 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partsnumber', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partsnumber',
            name='partnumber',
            field=models.CharField(max_length=200, unique=True, verbose_name='Parts Number'),
        ),
    ]