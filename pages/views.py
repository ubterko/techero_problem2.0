from django.shortcuts import render


def index(request):
	return render(request, 'pages/index.html', {})

def success(request):
	return render(request, 'pages/successpage.html', {})

def err(request):
	return render(request, 'pages/errorpage.html', {})
