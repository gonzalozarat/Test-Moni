# Generated by Django 3.2.7 on 2021-09-09 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0002_auto_20210204_0928'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loan',
            options={},
        ),
        migrations.AlterField(
            model_name='gender',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='loan',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
