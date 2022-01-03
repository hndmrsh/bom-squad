# Generated by Django 3.2.9 on 2022-01-03 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0017_rename_modulecomponentidentity_modulebomlistitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='modulebomlistitem',
            options={'verbose_name_plural': 'Module BOM List Items'},
        ),
        migrations.RenameField(
            model_name='module',
            old_name='component_identities',
            new_name='component_bom_list',
        ),
        migrations.AlterField(
            model_name='modulebomlistitem',
            name='designators',
            field=models.CharField(blank=True, help_text='A list of locations on the board.', max_length=255, null=True),
        ),
    ]
