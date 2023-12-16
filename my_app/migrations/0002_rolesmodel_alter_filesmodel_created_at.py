# Generated by Django 5.0 on 2023-12-16 19:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RolesModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 12, 17, 2, 28, 55, 953062))),
            ],
        ),
        migrations.AlterField(
            model_name='filesmodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 17, 2, 28, 55, 952646)),
        ),
    ]
