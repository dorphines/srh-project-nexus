from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import User, Location, Service, Session

class SRHApiTests(APITestCase):
    def setUp(self):
        # Create a staff user
        self.staff_user = User.objects.create_user(
            username='staff1', password='password123', role='staff'
        )
        self.client.force_authenticate(user=self.staff_user)

    def test_create_adolescent(self):
        url = reverse('adolescent-list')
        data = {
            'username': 'teen1',
            'password': 'password123',
            'first_name': 'Teen',
            'last_name': 'One',
            'role': 'adolescent',
            'date_of_birth': '2010-01-01',
            'gender': 'Female',
            'school': 'High School A'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(username='teen1').role, 'adolescent')

    def test_create_location(self):
        url = reverse('location-list')
        data = {
            'country': 'Kenya',
            'sub_county': 'Nairobi',
            'facility_name': 'Health Center A'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Location.objects.count(), 1)

    def test_full_flow(self):
        # 1. Create Location
        location = Location.objects.create(country='Kenya', sub_county='Nairobi', facility_name='Clinic B')
        
        # 2. Create Service
        url_service = reverse('service-list')
        response = self.client.post(url_service, {'name': 'Counseling', 'description': 'Talk therapy'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        service_id = response.data['id']

        # 3. Create Session
        url_session = reverse('session-list')
        data_session = {
            'location': location.id,
            'date': '2023-10-27',
            'topic': 'SRH Awareness'
        }
        response = self.client.post(url_session, data_session, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        session_id = response.data['id']

        # 4. Create Adolescent
        teen = User.objects.create_user(username='teen2', role='adolescent')

        # 5. Mark Attendance
        url_attendance = reverse('attendance-list')
        response = self.client.post(url_attendance, {'user': teen.id, 'session': session_id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # 6. Create Service Record
        url_record = reverse('servicerecord-list')
        data_record = {
            'user': teen.id,
            'service': service_id,
            'location': location.id,
            'description': 'Attended counseling'
        }
        response = self.client.post(url_record, data_record, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)