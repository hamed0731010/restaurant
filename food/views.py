from django.shortcuts import render ,get_object_or_404
from .models import food
from django.views.generic import DetailView
# Create your views here.
def food_list(request):
        food_list=food.objects.all()
        context={
        "foods":food_list
           }
        return render(request,"food/index.html",context)
# def food_detail(request, id):
#         food1 = food.objects.get(id=id)
#         context={
#          "food": food1
#         }
#         return  render(request,"food/food_detail.html",context)
class food_detail(DetailView):
        def get_object(self):
            return  get_object_or_404(food.objects.all(),id=self.kwargs.get("id"))


