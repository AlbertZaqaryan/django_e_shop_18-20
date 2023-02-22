from django.shortcuts import render
from django.views.generic import ListView
from .models import HomeSlider, HomeSliderActive, Category, SubCategory, Product
# Create your views here.

class HomeListView(ListView):
    template_name = 'main/index.html'

    def get(self, request):
        tertox = HomeSliderActive.objects.all()[0]
        tertvox = HomeSlider.objects.all()
        category_list = Category.objects.all()
        product_list = Product.objects.all()
        return render(request, self.template_name, context={
            'tertox':tertox,
            'tertvox':tertvox,
            'category_list':category_list,
            'product_list':product_list
        })
