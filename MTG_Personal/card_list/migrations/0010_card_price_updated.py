# Generated by Django 4.0.4 on 2022-06-01 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_list', '0009_alter_card_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='price_updated',
            field=models.BooleanField(default=False),
        ),
    ]
