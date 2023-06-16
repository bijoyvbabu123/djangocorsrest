from django.urls import path

from .views import SampleView

urlpatterns = [
    path('sampleview/', SampleView.as_view(), name='sampleview'), # sample view
    
]