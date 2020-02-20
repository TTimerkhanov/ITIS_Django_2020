from django.urls import path
from . import views

app_name = 'storage'
urlpatterns = [
    path('source/', views.SourceCreateView.as_view(), name='source-create'),
    path('source/list/', views.SourceListView.as_view(), name='source-list'),

    path('list/', views.ItemListView.as_view(), name='item-list'),
    path('<int:pk>/', views.ItemDetailView.as_view(), name='item-detail'),
    path('create/', views.ItemCreateView.as_view(), name='item-create'),
    path('<int:pk>/update/', views.ItemUpdateView.as_view(), name='item-update'),
    path('<int:pk>/delete/', views.ItemDelete.as_view(), name='item-delete'),
]
