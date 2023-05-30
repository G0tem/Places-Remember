from django.test import TestCase


class TestVisited(TestCase):
    def test_visited_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_visited_add(self):
        response = self.client.git('/addpost/')
        self.assertEqual(response.status_code, 302)