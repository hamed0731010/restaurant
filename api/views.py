from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateAPIView,ListCreateAPIView
from blog.models import blog
from .serializer import ArticleSerializer,UerSerializer
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User
from .permitions import IsSuperUser,IsStaffOrReadOnly,IsAuthorOrReadOnly,IsSuperUserOrStaffReadOnly,IsSuper
# Create your views here.
class AricleList(ListAPIView):
        queryset = blog.objects.all()
        serializer_class = ArticleSerializer
class Article_detail(RetrieveUpdateAPIView):
        queryset = blog.objects.all()
        serializer_class = ArticleSerializer
        permission_classes = (IsAuthorOrReadOnly,)
class UserDetail(RetrieveUpdateAPIView):
        queryset = User.objects.all()
        serializer_class = UerSerializer
        permission_classes = (IsStaffOrReadOnly,)
class UserList(ListCreateAPIView):
        queryset = User.objects.all()
        serializer_class = UerSerializer
        permission_classes = (IsStaffOrReadOnly,)