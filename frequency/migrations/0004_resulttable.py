# Generated by Django 2.2.7 on 2020-02-22 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frequency', '0003_auto_20200222_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='resulttable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Keyword', models.CharField(max_length=100)),
                ('wordfrequency', models.IntegerField()),
                ('URL', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frequency.givenurl')),
            ],
        ),
    ]
