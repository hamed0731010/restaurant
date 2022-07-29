from . import views
from  .views import food_detail
from django.urls import path
app_name="food"
urlpatterns=[

    path("",views.food_list,name="food_list"),
  #  path("<int:id>/",views.food_detail,name="detail")
    path("<int:id>/",food_detail.as_view(),name="detail")
]