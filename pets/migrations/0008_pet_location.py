# Generated by Django 2.0.3 on 2018-05-04 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0007_auto_20180504_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='location',
            field=models.CharField(default='', max_length=30),
        ),
    ]
