from django.db import models
from django.utils import  timezone
from django import forms
from mysite.settings import MEDIA_ROOT

class Post(models.Model):
    FOOD = 'FOO'
    BAR = 'BAR'
    PLACES = 'PLA'
    AVAILABLE_CATEGORIES = (
        (FOOD, 'Eat'),
        (BAR, 'Drink'),
        (PLACES, 'Where to go')
    )
    BURGER = 'BRG'
    TRADITIONAL = 'TRA'
    ASIAN = 'ASI'
    FASTFOOD = 'FAST'
    STREETFOOD = 'STR'
    CAKES = 'CAK'
    RANDOM = 'RAN'
    AVAILABLE_SUBCATEGORIES = (
        (BURGER, 'Burger'),
        (TRADITIONAL, 'Traditional'),
        (ASIAN, 'Asian'),
        (FASTFOOD, 'Fastfood'),
        (STREETFOOD, 'Streetfood'),
        (CAKES, 'Cakes'),
        (RANDOM, 'Random - to favourite')
    )
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=3, choices=AVAILABLE_CATEGORIES, default=FOOD)
    subcategory = models.CharField(max_length=3, choices=AVAILABLE_SUBCATEGORIES, default=BURGER)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to=MEDIA_ROOT, blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
