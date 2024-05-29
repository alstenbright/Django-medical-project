from django.urls import path,include
from homepage import views
urlpatterns = [
  path('', views.home, name='home'),
  path('products/',include('products.urls')),
  path('signup/',views.signup,name='signup'),
  path('login/',views.login_page,name='login'),
  path('medicoapi/', include('medicoapi.urls')),
  path('logout/', views.logout_view,name='logout'),
  
]