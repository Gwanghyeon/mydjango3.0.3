from django.urls import path
from . import views

# TEMPLATE URLS
app_name='basic_app'

urlpatterns=[
    path('',views.basic_app_index,name='basic_app_index'),
    path('register/',views.register,name='register'),  # name is required.
    path('user_login/',views.user_login,name='user_login'),
]