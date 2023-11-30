from django.contrib import admin
from django.urls import path, include
from recipes.views import home, contato, sobre


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls'))
]
