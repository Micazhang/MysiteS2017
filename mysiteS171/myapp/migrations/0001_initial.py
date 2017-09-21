# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-29 02:26
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import myapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('birthdate', models.DateField()),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('in_stock', models.BooleanField(default=True)),
                ('numpages', models.IntegerField(blank=True, null=True, validators=[myapp.models.validate_numpages])),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_no', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(default='Windsor', max_length=20)),
                ('province', models.CharField(choices=[('AB', 'Alberta'), ('MB', 'Manitoba'), ('ON', 'Ontario'), ('QC', 'Quebec')], default='ON', max_length=2)),
                ('age', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100, unique=True)),
                ('intro_course', models.BooleanField(default=True)),
                ('time', models.IntegerField(choices=[(0, 'No preference'), (1, 'Morning'), (2, 'Afernoon'), (3, 'Evening')], default=0)),
                ('num_responses', models.IntegerField(default=0)),
                ('avg_age', models.IntegerField(default=20)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, to='myapp.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='textbook',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Book'),
        ),
    ]