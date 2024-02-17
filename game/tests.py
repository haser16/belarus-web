from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class IndexTestCase(TestCase):
    def setUp(self) -> None:
        self.path = reverse('game:rools')

    def test_index(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Правила игры')
        self.assertTemplateUsed(response, 'game/rools.html')
