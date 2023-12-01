from django.urls import path, include
# from django.http import response
from recipes.views import home


urlpatterns = [
    path('', home),
]
