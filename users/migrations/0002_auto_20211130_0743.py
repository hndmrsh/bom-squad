# Generated by Django 3.2.9 on 2021-11-30 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('modules', '0007_alter_module_description'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExtended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('component_inventory', models.JSONField(null=True)),
                ('slug', models.SlugField(blank=True)),
                ('built_modules', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='built_modules', to='modules.module')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('want_to_build_modules', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='want_to_build_modules', to='modules.module')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
