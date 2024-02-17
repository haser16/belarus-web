from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from main.models import *


class IndexTestCase(TestCase):
    def setUp(self) -> None:
        self.path = reverse('main:index')

    def test_index(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Беларусь Современная')
        self.assertTemplateUsed(response, 'main/index.html')


class MedicineTestCase(TestCase):
    fixtures = ['medicine.json']

    def setUp(self) -> None:
        self.path = reverse('main:medicine')

    def test_index(self):
        response = self.client.get(self.path)

        text = Medicine.objects.all()

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Беларусь Современная - Медицина')
        self.assertEqual(response.context_data['path'], '/Главная/Медицина/')
        self.assertEqual(list(response.context_data['text']), list(text))
        self.assertTemplateUsed(response, 'main/category.html')


class IndustryTestCase(TestCase):
    fixtures = ['medicine.json']

    def setUp(self) -> None:
        self.path = reverse('main:industry')

    def test_index(self):
        response = self.client.get(self.path)

        text = Industry.objects.all()

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Беларусь Современная - Промышленность')
        self.assertEqual(response.context_data['path'], '/Главная/Промышленность/')
        self.assertEqual(list(response.context_data['text']), list(text))
        self.assertTemplateUsed(response, 'main/category.html')


class ConstructionTestCase(TestCase):
    fixtures = ['medicine.json']

    def setUp(self) -> None:
        self.path = reverse('main:construction')

    def test_index(self):
        response = self.client.get(self.path)

        text = Construction.objects.all()

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Беларусь Современная - Строительство')
        self.assertEqual(response.context_data['path'], '/Главная/Строительство/')
        self.assertEqual(list(response.context_data['text']), list(text))
        self.assertTemplateUsed(response, 'main/category.html')


class CarBuildingTestCase(TestCase):
    fixtures = ['medicine.json']

    def setUp(self) -> None:
        self.path = reverse('main:carbuilding')

    def test_index(self):
        response = self.client.get(self.path)

        text = CarBuilding.objects.all()

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Беларусь Современная - Промышленность(Машиностроение)')
        self.assertEqual(response.context_data['path'], '/Главная/Промышленность(Машиностроение)/')
        self.assertEqual(list(response.context_data['text']), list(text))
        self.assertTemplateUsed(response, 'main/category.html')


class AgricultureTestCase(TestCase):
    fixtures = ['medicine.json']

    def setUp(self) -> None:
        self.path = reverse('main:agriculture')

    def test_index(self):
        response = self.client.get(self.path)

        text = Agriculture.objects.all()

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Беларусь Современная - Сельское хозяйство')
        self.assertEqual(response.context_data['path'], '/Главная/Сельское хозяйство/')
        self.assertEqual(list(response.context_data['text']), list(text))
        self.assertTemplateUsed(response, 'main/category.html')


class ForestryTestCase(TestCase):
    fixtures = ['medicine.json']

    def setUp(self) -> None:
        self.path = reverse('main:forestry')

    def test_index(self):
        response = self.client.get(self.path)

        text = Forestry.objects.all()

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Беларусь Современная - Лесное хозяйство')
        self.assertEqual(response.context_data['path'], '/Главная/Лесное хозяйство/')
        self.assertEqual(list(response.context_data['text']), list(text))
        self.assertTemplateUsed(response, 'main/category.html')


class ITTestCase(TestCase):
    fixtures = ['medicine.json']

    def setUp(self) -> None:
        self.path = reverse('main:it')

    def test_index(self):
        response = self.client.get(self.path)

        text = IT.objects.all()

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Беларусь Современная - IT(Информационные технологии)')
        self.assertEqual(response.context_data['path'], '/Главная/IT(Информационные технологии)/')
        self.assertEqual(list(response.context_data['text']), list(text))
        self.assertTemplateUsed(response, 'main/category.html')


class CultureTestCase(TestCase):
    fixtures = ['medicine.json']

    def setUp(self) -> None:
        self.path = reverse('main:culture')

    def test_index(self):
        response = self.client.get(self.path)

        text = IT.objects.all()

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Беларусь Современная - Культура')
        self.assertEqual(response.context_data['path'], '/Главная/Культура/')
        self.assertEqual(list(response.context_data['text']), list(text))
        self.assertTemplateUsed(response, 'main/category.html')


class ArchitectureTestCase(TestCase):
    fixtures = ['medicine.json']

    def setUp(self) -> None:
        self.path = reverse('main:architecture')

    def test_index(self):
        response = self.client.get(self.path)

        text = IT.objects.all()

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Беларусь Современная - Архитектура')
        self.assertEqual(response.context_data['path'], '/Главная/Архитектура/')
        self.assertEqual(list(response.context_data['text']), list(text))
        self.assertTemplateUsed(response, 'main/category.html')

