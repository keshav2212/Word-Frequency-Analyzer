# Generated by Django 2.2.7 on 2020-02-22 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frequency', '0002_auto_20200221_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='givenurl',
            old_name='givenurl',
            new_name='URL',
        ),
    ]
