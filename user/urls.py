from django.urls import path, include
from rest_framework.routers import DefaultRouter
from user import views

app_name = 'user'

router = DefaultRouter()
router.register('', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]