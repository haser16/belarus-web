from django.urls import path

from game.views import RoolsTemplateView

app_name = 'game'

urlpatterns = [
    path('rools/', RoolsTemplateView.as_view(), name='rools'),
]
