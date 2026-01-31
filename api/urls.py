from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, AdolescentViewSet, LocationViewSet, ServiceViewSet, 
    SessionViewSet, ServiceRecordViewSet, FeedbackViewSet, AttendanceViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'adolescents', AdolescentViewSet, basename='adolescent')
router.register(r'locations', LocationViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'service-records', ServiceRecordViewSet)
router.register(r'feedback', FeedbackViewSet)
router.register(r'attendance', AttendanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
