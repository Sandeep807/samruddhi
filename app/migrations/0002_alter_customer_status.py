# Generated by Django 3.2.8 on 2021-11-01 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='status',
            field=models.CharField(choices=[('Aproved', 'Aproved'), ('Reject', 'Reject')], default='Pending', max_length=50),
        ),
    ]
