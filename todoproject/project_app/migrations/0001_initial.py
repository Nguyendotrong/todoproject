# Generated by Django 3.2.8 on 2021-11-05 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('completed_date', models.DateTimeField()),
                ('is_active', models.BooleanField()),
                ('project_manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='propjects_manager', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_date'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_date', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='UserProjects', to='project_app.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='UserProjects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
