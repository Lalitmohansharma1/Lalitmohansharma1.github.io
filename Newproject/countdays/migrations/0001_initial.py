# Generated by Django 3.2.9 on 2022-02-25 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='initialdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=2)),
                ('month', models.CharField(max_length=2)),
                ('year', models.CharField(max_length=4)),
                ('finalday', models.CharField(max_length=2)),
                ('finalmonth', models.CharField(max_length=2)),
                ('finalyear', models.CharField(max_length=4)),
            ],
        ),
    ]