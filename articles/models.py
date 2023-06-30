from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateField(auto_now_add=True)
    time_to_read = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.TextField(max_length=200)
    image = models.ImageField(default='default.jpg', upload_to='articles')
    text = models.TextField(max_length=20010911)

    def __str__(self):
        return f'{self.title} by {self.author} in {self.date_posted}'

    def get_absolute_url(self):
        return reverse('home')
