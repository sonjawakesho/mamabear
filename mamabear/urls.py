
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from pets import views as pets_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.login,name='login'),
    path('logout/', auth_views.logout,name='logout'),
    path('signup/',pets_views.signup, name='signup' ),
    path('home/', pets_views.home, name='home'),
    path('addpet/',pets_views.create_pet,name='add-pet'),
  
]