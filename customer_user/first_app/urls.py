from django.urls import path,include
from first_app import views

app_name = 'first_app'
urlpatterns = [
    path('',views.register,name='register'),
    path('login/',views.user_login,name='login'),
]