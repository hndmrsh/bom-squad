# Generated by Django 3.2.9 on 2022-01-02 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0013_auto_20211231_2226'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='modulecomponentidentity',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='modulecomponentidentity',
            name='bom_order',
        ),
    ]
