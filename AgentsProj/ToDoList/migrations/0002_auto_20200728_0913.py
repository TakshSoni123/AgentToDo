# Generated by Django 3.0.8 on 2020-07-28 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='agent_name',
            field=models.CharField(max_length=100),
        ),
    ]
