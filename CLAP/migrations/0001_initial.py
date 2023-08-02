# Generated by Django 3.2.6 on 2023-07-06 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CLAP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=50)),
                ('neighborhood', models.CharField(max_length=15)),
                ('birth_date_day', models.CharField(max_length=10)),
                ('birth_date_month', models.CharField(max_length=10)),
                ('birth_date_year', models.CharField(max_length=10)),
                ('age', models.CharField(max_length=10)),
            ],
        ),
    ]