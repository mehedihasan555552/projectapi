# Generated by Django 3.0.6 on 2020-06-03 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200604_0056'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='distance_in_miles',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='how_many_jobs',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='last_reviews',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default.jpg', max_length=200, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='account',
            name='specializes',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='stars_value',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_media',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
