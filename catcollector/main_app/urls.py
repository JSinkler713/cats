from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='index'),
    path('cats/new/', views.new_cat, name='new_cat'),
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
    path('cats/<int:cat_id>/update', views.cats_update, name='cats_update'),
    path('cats/<int:cat_id>/delete', views.cats_delete, name='cats_delete'),
    path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name="assoc_toy"),
    #------------------------------------------
    # full CRUD routes for Toys below:
    path('toys/', views.toy_index, name='toys_index'),
    # primary keys (or 'pk') is used instead of cat_id 
    # because Class-Based Views require it
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]
