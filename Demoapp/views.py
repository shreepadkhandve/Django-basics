from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
	print('hello')
	print('hello')
	print('hello')
	print('hello')
	print('hello')
	print('hello')
	return render(request,'homepage.html')
