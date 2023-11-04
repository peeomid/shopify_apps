from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.TextField()
    description = models.TextField(null=True, blank=True)
    url = models.TextField()

    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    featured_apps = models.ManyToManyField('App', blank=True)

class App(models.Model):
    name = models.TextField()
    url = models.TextField(unique=True)
    short_description = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    rating = models.FloatField()
    reviews = models.IntegerField()
    developer_url = models.TextField()
    pricing = models.TextField(null=True, blank=True)
    launched = models.DateField(null=True, blank=True)
    languages = models.TextField(null=True, blank=True)
    
    works_with = models.TextField(null=True, blank=True)
    review_summary = models.TextField(null=True, blank=True)

    categories = models.ManyToManyField(Category)
    developer = models.ForeignKey('Developer', on_delete=models.CASCADE)


class Review(models.Model):
    name = models.TextField()
    country = models.TextField(null=True, blank=True)
    time_used = models.TextField(null=True, blank=True)
    date = models.DateField()
    rating = models.FloatField()
    comment = models.TextField(null=True, blank=True)
    replied_date = models.DateField(null=True, blank=True)
    replied_comment = models.TextField(null=True, blank=True)

    app = models.ForeignKey(App, on_delete=models.CASCADE)

class Developer(models.Model):
    name = models.TextField()
    url = models.TextField()
    description = models.TextField(null=True, blank=True)
    number_of_apps = models.IntegerField()
    average_rating = models.FloatField()