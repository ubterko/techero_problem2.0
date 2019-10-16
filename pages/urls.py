from django.urls import path
from . import views

app_name = 'pages'
urlpatterns = [
	path('', views.index),
	path('successpage/', views.success),
	path('errorpage/', views.err),
	path('api/views/create_patron', views.CreateUserPatron.as_view(), name='create_patron'),
	path('api/views/create_proprietor', views.CreateUserProprietor.as_view(), name='create_proprietor'),
	path('api/views/proprietor_list', views.Proprietors.as_view(), name='proprietor_list'),
	path('api/views/auth', views.AuthView.as_view(), name='token')
]
