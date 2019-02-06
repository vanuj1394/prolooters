from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from datetime import datetime
from .models import product_iteam
import json
from .scrapper import parsor

def index(request):
	pars = parsor()
	pars.AmzonParser()
	product = product_iteam.objects.all()
	context = {
	 	'prod': product.values('title'),
	 }
	return render(request, 'proapp/index.html',context)
	# product.title = 'trimmer'
	# product.buy_link = 'https://www.amazon.in/Lifelong-LLPCM01-Trimmer-Cordless-Adjustment/dp/B07GSSFJLW/ref=sr_1_1_sspa?s=hpc&ie=UTF8&qid=1549086848&sr=1-1-spons&keywords=trimmer&psc=1'
	# product.img_src = 'https://images-eu.ssl-images-amazon.com/images/I/41QY58WjXSL._AC_US160_FMwebp_QL70_.jpg'
	# product.deal_price = '1200'
	# product.save()
	# context = {

	# 	'title': product.title,
	# 	'buylink':product.buy_link,


	# }
	# product = product_iteam.objects.all()
	# product = product_iteam(title = "" , buy_link ="" , img_src="" , deal_price="")
	
