# Generated by Django 2.2 on 2022-06-02 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advisor', '0002_auto_20210429_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceadvisor',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='serviceadvisor',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
    ]