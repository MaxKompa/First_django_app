from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('members/', include('members_app.urls')),  
    path('courses/', include('courses_app.urls')),  
]

