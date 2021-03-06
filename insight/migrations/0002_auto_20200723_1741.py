# Generated by Django 3.0.8 on 2020-07-23 17:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('insight', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('tag', models.TextField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2020, 7, 23, 17, 41, 0, 395149, tzinfo=utc))),
                ('first_used', models.CharField(default='', max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='keywords',
        ),
        migrations.AddField(
            model_name='account',
            name='primary_weight',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AddField(
            model_name='post',
            name='hobby_weight',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='account',
            name='joined_at',
            field=models.DateField(default=datetime.date(2020, 7, 23)),
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(db_index=True, default='', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='leaderboard',
            name='end_date',
            field=models.DateField(default=datetime.date(2020, 7, 23)),
        ),
        migrations.AlterField(
            model_name='leaderboard',
            name='start_date',
            field=models.DateField(default=datetime.date(2020, 7, 23)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 23, 17, 41, 0, 391206, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 23, 17, 41, 0, 387392, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='useractionref',
            name='date_created',
            field=models.DateField(default=datetime.date(2020, 7, 23)),
        ),
        migrations.AlterField(
            model_name='useractionref',
            name='time_created',
            field=models.TimeField(default=datetime.time(23, 11, 0, 389259)),
        ),
    ]
