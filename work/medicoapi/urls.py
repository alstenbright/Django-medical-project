from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
   
    path('signup',views.signup,name='signup_api'),
    path('login', views.login, name='login_api'),
    path('create', views.create, name='createapi'),
    path('list', views.list, name='retrieveproductapi'),
     path('<int:pk>/update', views.update, name='updateproductapi'),
      path('<int:pk>/delete', views.delete, name='deleteproductapi'),
       path('search/<str:Medicine_Name>/', views.search_medicine, name='search')
]

