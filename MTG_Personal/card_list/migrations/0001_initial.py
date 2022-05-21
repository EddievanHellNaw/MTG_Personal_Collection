# Generated by Django 4.0.4 on 2022-05-21 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('mana_cost', models.CharField(max_length=50)),
                ('mana_value', models.IntegerField(default=0)),
                ('card_type', models.CharField(max_length=200)),
                ('effect', models.CharField(max_length=1000)),
                ('expansion', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('rarity', models.CharField(max_length=200)),
                ('foil', models.BooleanField(verbose_name=False)),
                ('in_deck', models.BooleanField(verbose_name=False)),
                ('price', models.FloatField(default=0)),
            ],
        ),
    ]
