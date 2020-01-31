from django.shortcuts import render
from django.http import HttpResponse
from .models import Products,Blended_workshops
# Create your views here.
def index(request):
	products = Products.objects.all()
	workshops = Blended_workshops.objects.all()
	context = {'products':products,'workshops':workshops}
	return render(request,'spoken/index.html',context)