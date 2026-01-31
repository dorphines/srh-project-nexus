from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('adolescent', 'Adolescent'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='adolescent')
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    school = models.CharField(max_length=255, null=True, blank=True)

    @property
    def is_adolescent(self):
        return self.role == 'adolescent'

    @property
    def age(self):
        if self.date_of_birth:
            today = datetime.date.today()
            return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        return None

class Location(models.Model):
    country = models.CharField(max_length=100)
    sub_county = models.CharField(max_length=100)
    facility_name = models.CharField(max_length=255)

    def __str__(self):
        return self.facility_name

class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Session(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateField()
    topic = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.topic} at {self.location}"

class ServiceRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='services_received')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    date_assessed = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True)

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField()

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('user', 'session')