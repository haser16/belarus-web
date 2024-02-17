from django.views.generic.base import TemplateView

from common.views import IconMixin, TitleMixin
from game.models import Icons


class RoolsTemplateView(IconMixin, TitleMixin, TemplateView):
    template_name = 'game/rools.html'
    title = 'Правила Игры'
    icons_elem = Icons.objects.all()
