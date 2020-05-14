from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('models/', include('models_page.urls')),
    path('admin/', admin.site.urls),
]
