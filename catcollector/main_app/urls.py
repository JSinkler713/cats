from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='index'),
    path('cats/new/', views.new_cat, name='new_cat'),
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
    path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    #------------------------------------------
    # full CRUD routes for Toys below:
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    # primary keys (or 'pk') is used instead of cat_id 
    # because Class-Based Views require it
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]
