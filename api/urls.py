from django.urls import path,include
from .views import AricleList,Article_detail,UserList,UserDetail

app_name="api"
urlpatterns=[
    path("", AricleList.as_view(), name='list'),
    path("<int:pk>", Article_detail.as_view(), name='detail'),
    path("user", UserList.as_view(), name='listuser'),
    path("user/<int:pk>", UserDetail.as_view(), name='detailuser'),
]