# Generated by Django 3.2.6 on 2021-09-03 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20210901_2321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('timeline', models.DateTimeField()),
                ('task_created_date', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.employee')),
            ],
            options={
                'db_table': 'task',
            },
        ),
    ]
