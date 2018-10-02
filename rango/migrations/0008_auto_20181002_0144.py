# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-02 01:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_profilegreetedbyactiveuser_profilelikedbyactiveuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilegreetedbyactiveuser',
            name='liker',
        ),
        migrations.RemoveField(
            model_name='profilelikedbyactiveuser',
            name='greeter',
        ),
        migrations.AlterField(
            model_name='profilegreetedbyactiveuser',
            name='greeter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='greeter', to='rango.UserProfile'),
        ),
        migrations.AlterField(
            model_name='profilelikedbyactiveuser',
            name='liker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liker', to='rango.UserProfile'),
        ),
    ]
