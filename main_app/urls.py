from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name= 'about'),
    path('places/', views.places_index, name='index'),
    path('places/<int:place_id>/', views.places_detail, name='places_detail'),
    path('places/create/', views.PlaceCreate.as_view(), name='places_create'),
    path('places/<int:pk>/update/', views.PlaceUpdate.as_view(), name='places_update'),
    path('places/<int:pk>/delete/', views.PlaceDelete.as_view(), name='places_delete'),
    path('places/<int:place_id>/add_review/', views.add_review, name='add_review'),

    path('attractions/', views.AttractionList.as_view(), name='attractions_index'), 
    path('attractions/<int:pk>/', views.AttractionDetail.as_view(), name='attractions_detail'),

    path('attractions/create/', views.AttractionCreate.as_view(), name='attractions_create'),

    path('attractions/<int:pk>/update/',views.AttractionUpdate.as_view(), name='attractions_update'),
    path('attractions/<int:pk>/delete/', views.AttractionDelete.as_view(), name='attractions_delete'),


    path('places/<int:place_id>/assoc_attraction/<int:attraction_id>/', views.assoc_attraction, name='assoc_attraction'),
    path('places/<int:place_id>/unassoc_attraction/<int:attraction_id>/', views.unassoc_attraction, name='unassoc_attraction'),
   


]