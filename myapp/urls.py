from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_login, name='login'),  # Mapeia a URL raiz para a view 'login
    path('forgot_password', views.forgot_password_view, name='forgot_password'),
    path('create_account', views.create_account_view, name='create_account'),
]