# Generated by Django 5.0.6 on 2024-07-05 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='Category',
        ),
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.ManyToManyField(to='tasks.category'),
        ),
    ]
