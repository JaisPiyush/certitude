# Generated by Django 3.0.8 on 2020-08-19 12:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('insight', '0014_auto_20200817_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='joined_at',
            field=models.DateField(default=datetime.date(2020, 8, 19)),
        ),
        migrations.AlterField(
            model_name='actionstore',
            name='loved_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 12, 38, 3, 319294, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='actionstore',
            name='viewed_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 12, 38, 3, 319439, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leaderboard',
            name='end_date',
            field=models.DateField(default=datetime.date(2020, 8, 19)),
        ),
        migrations.AlterField(
            model_name='leaderboard',
            name='start_date',
            field=models.DateField(default=datetime.date(2020, 8, 19)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 12, 38, 3, 320950, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 12, 38, 3, 315235, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='tags',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 12, 38, 3, 324959, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='useractionref',
            name='date_created',
            field=models.DateField(default=datetime.date(2020, 8, 19)),
        ),
        migrations.AlterField(
            model_name='useractionref',
            name='time_created',
            field=models.TimeField(default=datetime.time(18, 8, 3, 316990)),
        ),
    ]