from django.contrib import admin
from .models import blog ,category,tag,comments
# Register your models here.
admin.site.register(blog)
admin.site.register(category)
admin.site.register(tag)
admin.site.register(comments)