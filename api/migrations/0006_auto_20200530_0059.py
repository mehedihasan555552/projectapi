# Generated by Django 3.0.6 on 2020-05-29 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200530_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='job',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
