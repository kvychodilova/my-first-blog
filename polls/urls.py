from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('cat/<str:categ_name>/', views.filter_books,name='nextview')
]