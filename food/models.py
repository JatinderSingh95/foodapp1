# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings




MY_CHOICES = (
    ('Open', 'Open'),
    ('Opening Soon', 'Opening Soon'),
    
    
)

OPTIONS = (
                ("AUT", "Breakfast"),
                ("DEU", "Lunch"),
                ("NLD", "Dinner"),
                )

class Blog(models.Model):
    
	restaurant = models.CharField(max_length=100, unique=False)
	address = models.CharField(max_length=100, unique=False)
	locations = models.CharField(max_length=100, unique=False)
	pincode = models.IntegerField()
	landmark = models.CharField(max_length=100, unique=False)
	restaurantphn = models.CharField(max_length=100, unique=False)
	restaurantemail = models.EmailField()
	openingstatus = models.CharField(max_length=60,choices=MY_CHOICES)
	restaurantweb = models.CharField(max_length=100, unique=False)
	first_aid = models.BooleanField(default=False)
	


def __unicode__(self):
        return self.title

def get_absolute_url(self):
        return reverse('server_edit', kwargs={'pk': self.pk})
		
