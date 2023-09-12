from django.urls import path

from . import views
app_name = 'movieapp'
urlpatterns=[
    path('',views.index,name='index'),
    path('details/<int:movie_id>/', views.detail, name='detail'),
    path('add/', views.movie_add, name='movie_add'),
    path('update/<int:movie_id>/', views.update, name='update'),
    path('delete/<int:movie_id>/', views.delete, name='delete'),

]