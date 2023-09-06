from django.db import models


class Category(models.Model):
    """
    Category model
    Stores categories
    """
    CATEGORIES = [
        ('sport', 'SPORT'),
        ('music', 'MUSIC'),
        ('culture', 'CULTURE'),
        ('books', 'BOOKS'),
        ('education', 'EDUCATION'),
        ('business', 'BUSINESS'),
        ('fitness', 'FITNESS'),
        ('food_drink', 'FOOD AND DRINK'),
        ('games', 'GAMES'),
    ]

    category = models.CharField(max_length=30, choices=CATEGORIES)
