from django.contrib import admin
from django.urls import path
from reports.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
]
