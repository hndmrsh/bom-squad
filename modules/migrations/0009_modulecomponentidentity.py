# Generated by Django 3.2.9 on 2021-12-27 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0003_auto_20211112_1447'),
        ('modules', '0008_module_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModuleComponentIdentity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component', models.ManyToManyField(to='components.Component')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='modules.module')),
            ],
        ),
    ]
