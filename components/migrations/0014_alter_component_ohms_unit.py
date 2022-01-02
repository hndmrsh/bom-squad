# Generated by Django 3.2.9 on 2022-01-02 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0013_auto_20220102_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='ohms_unit',
            field=models.CharField(blank=True, choices=[('Ω', 'Ω'), ('kΩ', 'kΩ'), ('MΩ', 'MΩ')], help_text='If the component type involves resistance, this value MUST be set.', max_length=2, null=True),
        ),
    ]
