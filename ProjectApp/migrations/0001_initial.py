# Generated by Django 3.1.5 on 2022-03-21 10:38

import ProjectApp.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CoreApp', '0001_initial'),
        ('AdminApp', '0001_initial'),
        ('ChatApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveKvantProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.ManyToManyField(blank=True, to='ChatApp.ChatMessage')),
            ],
            options={
                'db_table': 'active_project',
            },
        ),
        migrations.CreateModel(
            name='KvantProjectMembershipRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'member_request',
            },
        ),
        migrations.CreateModel(
            name='MemberHiringKvantProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ProjectApp.activekvantproject')),
                ('requests', models.ManyToManyField(blank=True, to='ProjectApp.KvantProjectMembershipRequest')),
            ],
            options={
                'db_table': 'hiring_project',
            },
        ),
        migrations.CreateModel(
            name='KvantProjectTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('deadline', models.DateField(blank=True)),
                ('title', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[('Бэклог', 'Бэклог'), ('Задачи', 'Задачи'), ('В прогрессе', 'В прогрессе'), ('Выполнено', 'Выполнено'), ('Архив', 'Архив')], default='Бэклог', max_length=100)),
                ('priority', models.CharField(choices=[('low', 'Низкий'), ('high', 'Высокий'), ('medium', 'Средний'), ('none', 'Нет')], default='none', max_length=100)),
                ('files', models.ManyToManyField(blank=True, to='CoreApp.FileStorage')),
                ('participants', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'project_task',
            },
        ),
        migrations.CreateModel(
            name='KvantProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('image', models.ImageField(default=ProjectApp.models.setDefaultImage, upload_to=ProjectApp.models.getPath)),
                ('course_subject', models.ManyToManyField(to='AdminApp.KvantCourseType')),
                ('files', models.ManyToManyField(blank=True, to='CoreApp.FileStorage')),
                ('tasks', models.ManyToManyField(blank=True, to='ProjectApp.KvantProjectTask')),
                ('team', models.ManyToManyField(blank=True, related_name='team', to=settings.AUTH_USER_MODEL)),
                ('teamleader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teamleader', to=settings.AUTH_USER_MODEL)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'kvant_project',
                'ordering': ['-date', '-id'],
            },
        ),
        migrations.CreateModel(
            name='ClosedKvantProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(default=django.utils.timezone.now)),
                ('project', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ProjectApp.kvantproject')),
            ],
            options={
                'db_table': 'closed_project',
            },
        ),
        migrations.AddField(
            model_name='activekvantproject',
            name='project',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ProjectApp.kvantproject'),
        ),
    ]
