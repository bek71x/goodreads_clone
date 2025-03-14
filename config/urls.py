
from django.contrib import admin
from django.urls import path, include

from config.views import landing_page

app_name = "users"

urlpatterns = [
    path('', landing_page, name = 'landing_page'),
    path('users/',include('users.urls')),
    path('admin/', admin.site.urls),
]

