# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime    


# Create your models here.
class product_iteam(models.Model):
	
	title = models.CharField(max_length=400)
	buy_link=models.CharField(max_length=300)
	img_src = models.CharField(max_length=300)
	deal_price = models.CharField(max_length=300)
	date = models.DateTimeField(default=datetime.now, blank=True)


	class Meta:
		unique_together = unique_together = (("title"),("deal_price"),)


	def __str__(self):
		return self.title 



