from django.urls import path
from .views import CreateAccountView
# from .views import profile

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),
name='createAccount'),
]

# urlpatterns = [

#     path('profile/', profile, name='users-page'),
# ]