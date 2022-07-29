from blog.models import blog
from rest_framework import serializers
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
        class Meta:
                model=blog
                fields="__all__"
class UerSerializer(serializers.ModelSerializer):
        class Meta:
                model=User
                fields="__all__"