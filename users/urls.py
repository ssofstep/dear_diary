from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import RegisterView

app_name = 'users'

urlpatterns = [
    path('users/register', RegisterView.as_view(), name='register'),
    path('users/login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('users/logout', LogoutView.as_view(next_page='diary:note_list'), name='logout'),

]
