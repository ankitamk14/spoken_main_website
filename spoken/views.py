from django.shortcuts import render
from django.http import HttpResponse
from .models import Products,Blended_workshops
# Create your views here.
def index(request):
	products = Products.objects.all()
	context = {'products':products}
	return render(request,'spoken/index.html',context)