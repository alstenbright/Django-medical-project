from . import views
from django.urls import path

urlpatterns = [
          path('create/',views.create,name='create'),
          path('retrieve/',views.read,name='medicoretrieve'),
          path('update/<int:id>/',views.update,name='update'),
          path('delete/<int:pk>',views.delete,name='delete'),
          path('products/retrieve/', views.medical_list, name='product_list'),

    ]