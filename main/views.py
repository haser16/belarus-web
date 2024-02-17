from django.views.generic.base import TemplateView

from common.views import *
from main.models import *


class IndexTemplateView(TitleMixin, TemplateView):
    template_name = 'main/index.html'
    title = 'Беларусь Современная'


class MedicineTemplateView(ImageMixin, TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Медицина'
    path = '/Главная/Медицина/'
    model_text = Medicine.objects.all()
    image = Images.objects.get(name='Медицина')


class IndustryTemplateView(ImageMixin, TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Промышленность'
    path = '/Главная/Промышленность/'
    model_text = Industry.objects.all()
    image = Images.objects.get(name='Промышленность')


class ConstructionTemplateView(ImageMixin, TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Строительство'
    path = '/Главная/Строительство/'
    model_text = Construction.objects.all()
    image = Images.objects.get(name='Строительство')


class CarBuildingTemplateView(ImageMixin, TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Промышленность(Машиностроение)'
    path = '/Главная/Промышленность(Машиностроение)/'
    model_text = Construction.objects.all()
    image = Images.objects.get(name='Машиностроение')


class AgricultureTemplateView(ImageMixin, TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Сельское хозяйство'
    path = '/Главная/Сельское хозяйство/'
    model_text = Agriculture.objects.all()
    image = Images.objects.get(name='Сельское хозяйство')


class ForestryTemplateView(ImageMixin, TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Лесное хозяйство'
    path = '/Главная/Лесное хозяйство/'
    model_text = Forestry.objects.all()
    image = Images.objects.get(name='Лесное хозяйство')


class ITTemplateView(ImageMixin, TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - IT(Информационные технологии)'
    path = '/Главная/IT(Информационные технологии)/'
    model_text = IT.objects.all()
    image = Images.objects.get(name='IT')


class CultureTemplateView(ImageMixin, TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Культура'
    path = '/Главная/Культура/'
    model_text = Culture.objects.all()
    image = Images.objects.get(name='Культура')


class ArchitectureTemplateView(ImageMixin, TitleMixin, PathMixin, ModelMixin, TemplateView):
    template_name = 'main/category.html'
    title = 'Беларусь Современная - Архитектура'
    path = '/Главная/Архитектура/'
    model_text = Architecture.objects.all()
    image = Images.objects.get(name='Архитектура')
