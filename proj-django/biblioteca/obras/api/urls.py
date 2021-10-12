from django.urls import path
from . import views

app_name = 'obras'

urlpatterns = [
    path('obras/', views.ObrasListView.as_view(), name='obras_list'),
    path('obras/<pk>/', views.ObrasDetailView.as_view(), name='obras_detail'),
]