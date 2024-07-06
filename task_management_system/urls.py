
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showTask, name='show_task'),
    path('tasks/', include('tasks.urls')),
    path('categories/', include('categories.urls')),
]
