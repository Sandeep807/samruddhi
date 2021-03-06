# Generated by Django 3.2.8 on 2021-11-12 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='releasing',
        ),
        migrations.RemoveField(
            model_name='releasecustomer',
            name='gross_amount',
        ),
        migrations.RemoveField(
            model_name='releasecustomer',
            name='margin',
        ),
        migrations.RemoveField(
            model_name='releasecustomer',
            name='net_amount',
        ),
        migrations.RemoveField(
            model_name='releasecustomer',
            name='paid_amount',
        ),
        migrations.RemoveField(
            model_name='releasecustomer',
            name='release_amount',
        ),
        migrations.RemoveField(
            model_name='releasecustomer',
            name='release_amount1',
        ),
        migrations.RemoveField(
            model_name='releasecustomer',
            name='stone_weight',
        ),
        migrations.AddField(
            model_name='releasecustomer',
            name='mobile_number',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='releasecustomer',
            name='name',
            field=models.CharField(default=3, max_length=50),
            preserve_default=False,
        ),
    ]
