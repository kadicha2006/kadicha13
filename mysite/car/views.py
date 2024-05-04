from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Car
from .forms import CarForm
from django.urls import reverse_lazy

class CarListView(ListView):
    model = Car
    queryset = Car.objects.all()
    template_name = 'car_list.html'
    context_object_name = 'cars'

class CarDetailView(DetailView):
    model = Car
    queryset = Car.objects.all()
    template_name = 'car_detail.html'
    context_object_name = 'car'

class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'car_create.html'
    success_url = reverse_lazy('car_list')

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car_update.html'
    success_url = reverse_lazy('car_list')

class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = reverse_lazy('car_list')


