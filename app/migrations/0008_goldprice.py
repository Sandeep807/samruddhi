# Generated by Django 3.2.8 on 2021-11-02 15:59

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20211101_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoldPrice',
            fields=[
                ('gold_id', models.IntegerField(default=app.models.generate_gold_id, editable=False, primary_key=True, serialize=False)),
                ('price', models.FloatField()),
            ],
        ),
    ]
