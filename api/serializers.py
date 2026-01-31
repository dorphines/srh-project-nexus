from rest_framework import serializers
from .models import User, Location, Service, Session, ServiceRecord, Feedback, Attendance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'role', 'date_of_birth', 'gender', 'school', 'is_adolescent', 'age']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class AdolescentSerializer(UserSerializer):
    def create(self, validated_data):
        validated_data['role'] = 'adolescent'
        return super().create(validated_data)

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class ServiceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRecord
        fields = '__all__'

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
