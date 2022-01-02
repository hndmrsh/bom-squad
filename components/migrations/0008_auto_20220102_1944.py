# Generated by Django 3.2.9 on 2022-01-02 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0007_auto_20220102_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='component',
            name='supplier_item_no',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='component',
            name='tolerance',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='component',
            name='voltage_rating',
            field=models.CharField(blank=True, max_length=3),
        ),
        migrations.AlterField(
            model_name='componentmanufacturer',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='types',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
