from rest_framework import viewsets
from .models import User, Location, Service, Session, ServiceRecord, Feedback, Attendance
from .serializers import (
    UserSerializer, AdolescentSerializer, LocationSerializer, 
    ServiceSerializer, SessionSerializer, ServiceRecordSerializer, 
    FeedbackSerializer, AttendanceSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AdolescentViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(role='adolescent')
    serializer_class = AdolescentSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class ServiceRecordViewSet(viewsets.ModelViewSet):
    queryset = ServiceRecord.objects.all()
    serializer_class = ServiceRecordSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer