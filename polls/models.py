from tkinter import CASCADE
from django.db import models


class Poll(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)

    def __str__(self):
        
        return "{0} (Slug: {1})".format(self.name, self.slug)
        # return self.name


class Choice(models.Model):
    poll = models.ForeignKey(to='Poll', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{0}: {1}".format(self.poll.name, self.name)

class Teilnehmer(models.Model):
    name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    thema = models.TextField(blank=True, null=True)

    
    def __str__(self):
        return f"{self.name},{self.email}, {self.thema}"