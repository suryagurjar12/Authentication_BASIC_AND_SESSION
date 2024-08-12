from django.urls import path,include
from .views import *
from rest_framework import routers
from rest_framework.authtoken import views


router = routers.DefaultRouter()
router.register(r'school',SchoolViewSet, basename='school')
router.register(r'Student',StudentViewSet,basename='Student')

urlpatterns = [
    path('api/',include(router.urls)),
    # path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token)
]
