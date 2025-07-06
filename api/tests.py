from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

class HealthViewTest(APITestCase):
    def test_health_view(self):
        url = reverse('health')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"status": "ok"})
