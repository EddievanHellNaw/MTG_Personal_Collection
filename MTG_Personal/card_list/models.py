from django.db import models

# Create your models here.
class Card(models.Model):
    quantity = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    effect = models.CharField(max_length=1000, null=True)
    mana_value = models.IntegerField(default=0)
    expansion_name = models.CharField(max_length=100, null=True)
    card_type = models.CharField(max_length=200, null=True)
    color = models.CharField(max_length=200, null=True)
    card_pic = models.ImageField(upload_to='media/', null=True)
    card_condition = models.CharField(max_length=100, null=True)
    foil = models.BooleanField(default=False)
    in_deck = models.BooleanField(default=False)
    price = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name
    
