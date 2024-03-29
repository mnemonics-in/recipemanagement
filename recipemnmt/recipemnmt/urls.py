"""
URL configuration for recipemnmt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from recipeapp import views


from rest_framework.authtoken import views as rviews #import alisaing
from rest_framework.routers import SimpleRouter
router=SimpleRouter()
router.register('recipes',views.AllRecipe)
router.register('user',views.CreateUser)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipe/', include(router.urls)),
    # path('recipe/',include('recipeapp.urls')),
    path('search/', include('searchapp.urls')),
    path('recipe/', include('rateapp.urls')),
    path('api-token-auth/', rviews.obtain_auth_token),  # Login view
    path('user_logout', views.user_logout.as_view(), name="user_logout"),

]
