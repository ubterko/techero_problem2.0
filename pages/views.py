from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'pages/index.html', {})

def success(request):
	return render(request, 'pages/successpage.html', {})

def err(request):
	return render(request, 'pages/errorpage.html', {})

