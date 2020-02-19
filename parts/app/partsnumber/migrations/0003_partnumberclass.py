# Generated by Django 2.1 on 2020-02-18 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partsnumber', '0002_auto_20200217_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartNumberClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('class_name', models.CharField(max_length=20, verbose_name='Class name')),
                ('charge_type', models.CharField(max_length=20, verbose_name='Charge Type')),
                ('code_name', models.CharField(max_length=7, unique=True, verbose_name='Code Name/Code Number')),
            ],
            options={
                'verbose_name': 'Part Number Class',
                'verbose_name_plural': 'Part Number Classes',
                'db_table': 'partnumber_class',
                'ordering': ['id'],
            },
        ),
    ]