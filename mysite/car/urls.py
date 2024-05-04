from.views import CarListView
from django.urls import path, include


urlpatterns = [
    path('', CarListView.as_view(),name='car_list')

]