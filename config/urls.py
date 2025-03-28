from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from config.views import landing_page, home

app_name = "users"

urlpatterns = [
    path('', landing_page, name = 'landing_page'),
    path('home/', home, name = 'home'),
    path('users/',include('users.urls')),
    path('admin/', admin.site.urls),
    path('books/', include('book.urls')),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
