from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('number.urls')),
    path('admin/', admin.site.urls),
]

handler404 = 'number.views.handle_page_not_found'
