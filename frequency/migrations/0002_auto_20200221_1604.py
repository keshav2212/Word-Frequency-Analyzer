# Generated by Django 2.2.7 on 2020-02-21 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frequency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='givenurl',
            name='result',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
