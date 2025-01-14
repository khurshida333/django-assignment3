# Generated by Django 5.0.6 on 2024-07-05 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Task_Title', models.CharField(max_length=50)),
                ('Task_Description', models.TextField()),
                ('Is_Completed', models.BooleanField(default=False)),
                ('Task_Assign_Date', models.DateField()),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.category')),
            ],
        ),
    ]
