# Generated by Django 3.2.9 on 2022-01-03 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0018_auto_20220103_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulebomlistitem',
            name='type',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
