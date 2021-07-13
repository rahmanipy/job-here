# Generated by Django 3.2.5 on 2021-07-13 08:01

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
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marital_status', models.CharField(blank=True, choices=[('M', 'married'), ('S', 'single')], max_length=50, null=True)),
                ('military_status', models.CharField(blank=True, choices=[('I', 'included'), ('E', 'end'), ('PE', 'permanent exemption'), ('EE', 'education exemption'), ('S', 'serving')], max_length=50, null=True)),
                ('job_status', models.CharField(blank=True, choices=[('E', 'employed'), ('JS', 'job seeker'), ('LFBJ', 'looking for better job')], max_length=70, null=True)),
                ('job_type', models.CharField(blank=True, choices=[('F', 'full time'), ('P', 'part time'), ('I', 'internship'), ('R', 'remote')], max_length=70, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('is_show_for_employers', models.BooleanField(default=False)),
                ('avatar', models.ImageField(default='default_employee_avatar.jpg', upload_to='')),
                ('about_me', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(limit_choices_to={'is_active': True, 'is_employer': False}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
