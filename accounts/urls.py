from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
    # include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # registration page
    path('create_account/', views.create_account, name='create-account'),
]