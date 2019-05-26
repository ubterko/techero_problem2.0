from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('successpage/', views.success),
	path('errorpage/', views.err),
]