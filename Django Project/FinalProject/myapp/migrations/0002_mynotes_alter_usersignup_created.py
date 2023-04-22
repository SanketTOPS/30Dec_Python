# Generated by Django 4.2 on 2023-04-22 04:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mynotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 22, 10, 8, 35, 878803))),
                ('title', models.CharField(max_length=100)),
                ('cate', models.CharField(max_length=50)),
                ('files', models.FileField(upload_to='myfiles')),
                ('comments', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='usersignup',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 4, 22, 10, 8, 35, 877802)),
        ),
    ]
