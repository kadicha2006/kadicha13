from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_name','price,marka' ,'model','category' ,'description' ,'date' ,'year','type' ,'volume','image' ,'volume']