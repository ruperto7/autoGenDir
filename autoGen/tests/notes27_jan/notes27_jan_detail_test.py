from django.test import TestCase
from django.urls import reverse

class Notes27JanDetailTestCase(TestCase):
    def setUp(self):
        pass

    def test_notes27_jan_detail_page(self):
        response = self.client.get(reverse('notes27_jan_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes27_jan/notes27_jan_detail.html')