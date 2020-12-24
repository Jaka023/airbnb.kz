from django.urls import path
from .views import AppartmentsList, AppartmentDetail

urlpatterns = [
    path('', AppartmentsList.as_view(), name='appartments_list'),
    path('<int:pk>/', AppartmentDetail.as_view(), name='detail'),
]