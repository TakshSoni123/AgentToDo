# Generated by Django 3.0.8 on 2020-07-28 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_name', models.CharField(max_length=50)),
                ('agent_id', models.CharField(max_length=5)),
                ('agent_pass', models.CharField(max_length=256)),
            ],
            options={
                'db_table': 'agent_auth',
            },
        ),
    ]
