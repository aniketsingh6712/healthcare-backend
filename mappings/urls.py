from django.urls import path
from .views import MappingListCreateView, MappingDetailPatientView

urlpatterns = [
    path('', MappingListCreateView.as_view()),        
    path('<int:id>/', MappingDetailPatientView.as_view()),  
]
