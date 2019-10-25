from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
	path('', views.index),
	path('successpage/', views.success),
	path('errorpage/', views.err),
]
