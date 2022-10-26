from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.halaman),
    path('learn/', include('learn.urls')),
    path('community/', include('community.urls')),
    path('exchanges/', include('exchanges.urls')),
]
