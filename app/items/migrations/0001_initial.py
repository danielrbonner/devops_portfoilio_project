# Generated by Django 3.2.2 on 2022-01-27 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_description', models.CharField(default='', max_length=250)),
                ('upc', models.CharField(default='', max_length=200)),
                ('language', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
