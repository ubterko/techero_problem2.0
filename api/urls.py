from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='registration'),
	path('register_patron/', views.CreatePatronView.as_view(), name='create_patron'),
	path('register_proprietor/', views.CreateProprietorView.as_view(), name='create_proprietor'),
	path('home/', views.Home.as_view(), name='home'),
	path('auth/', views.AuthView.as_view(), name='auth'),
	path('proprietor/<int:pk>/', views.ProprietorProfile.as_view(), name='proprietor_profile'),
	path('patron/<int:pk>/', views.PatronProfile.as_view(), name='patron_profile'),
	path('trip/',views.SetTrip.as_view(), name='book'),
	#path('/user_dashboard', views.Dashboard.as_view(), name='dashboard')
]
