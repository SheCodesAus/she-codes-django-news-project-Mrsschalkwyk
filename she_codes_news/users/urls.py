from django.urls import path
from .views import CreateAccountView
from .views import UserProfile

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('Profile/', UserProfile.as_view(), name='profile'),

]

