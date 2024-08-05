from django.contrib import admin
from django.urls import path
from myapp.views import HelloWorldView, UserCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    path('create-user/', UserCreate.as_view(), name='create_user'),
]
