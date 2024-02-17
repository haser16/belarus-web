from django.urls import path

from main.views import (AgricultureTemplateView, ArchitectureTemplateView,
                        CarBuildingTemplateView, ConstructionTemplateView,
                        CultureTemplateView, ForestryTemplateView,
                        IndexTemplateView, IndustryTemplateView,
                        ITTemplateView, MedicineTemplateView)

app_name = 'main'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('medicine/', MedicineTemplateView.as_view(), name='medicine'),
    path('industry/', IndustryTemplateView.as_view(), name='industry'),
    path('construction/', ConstructionTemplateView.as_view(), name='construction'),
    path('carbuilding/', CarBuildingTemplateView.as_view(), name='carbuilding'),
    path('agriculture/', AgricultureTemplateView.as_view(), name='agriculture'),
    path('forestry/', ForestryTemplateView.as_view(), name='forestry'),
    path('it/', ITTemplateView.as_view(), name='it'),
    path('culture/', CultureTemplateView.as_view(), name='culture'),
    path('architecture/', ArchitectureTemplateView.as_view(), name='architecture'),
]
