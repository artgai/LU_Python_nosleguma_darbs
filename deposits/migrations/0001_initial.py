# Generated by Django 3.2.2 on 2021-05-11 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit', models.FloatField()),
                ('term', models.FloatField()),
                ('rate', models.FloatField()),
            ],
        ),
    ]
