from django.urls import path, include
# from django.http import response
from recipes.views import home, contato, sobre


urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato)
]
