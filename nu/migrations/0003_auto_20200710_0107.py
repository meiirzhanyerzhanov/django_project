# Generated by Django 3.0.7 on 2020-07-09 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nu', '0002_auto_20200710_0047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='nu.Student'),
        ),
    ]
