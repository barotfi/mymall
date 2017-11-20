from django.db import models
from django.contrib.auth.models import User

class Stores(models.Model):
    FOOD = 'Food'
    ELECTRONIC = 'Electronic'
    TRAVEL = 'Travel'

    CATEGORY_CHOICES = (
        (FOOD, "Food"),
        (ELECTRONIC, "Electronic"),
        (TRAVEL, "Travel"),
        )

    category = models.CharField(max_length=15,
                  choices=CATEGORY_CHOICES,
                  default=FOOD)
    #category = models.CharField(max_length=200)
    storename = models.CharField(max_length=200)
    store_link = models.URLField(max_length=200)
    store_username = models.CharField(max_length=200)
    store_pw = models.CharField(max_length=200)
    last_updated = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, null=True, related_name='+')

    def __str__(self):
        return self.category
