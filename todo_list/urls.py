from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name= 'about'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('edit/<list_id>', views.edit, name='edit'),
    path('activate/<list_id>', views.activate, name='activate'),
    path('deactivate/<list_id>', views.deactivate, name='deactivate')
]
