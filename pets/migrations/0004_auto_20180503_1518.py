# Generated by Django 2.0.3 on 2018-05-03 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0003_pet_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='age',
            field=models.CharField(default='', max_length=30),
        ),
    ]
