from django.db import models

# Create your models here.
class Card(models.Model):
    quantity = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    mana_cost = models.CharField(max_length=50)
    mana_value = models.IntegerField(default=0)
    card_type = models.CharField(max_length=200)
    effect = models.CharField(max_length=1000)
    expansion = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    rarity = models.CharField(max_length=200)
    foil = models.BooleanField(default=False)
    in_deck = models.BooleanField(default=False)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name
    
