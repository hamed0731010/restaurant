from  . import views
from django.urls import path
app_name="blog"
urlpatterns=[

    path("",views.blog_list,name="blog_list"),
    path("<int:id>/",views.blog_detail,name="detail"),
    path("tag/<slug:tag>",views.blog_tag,name="tag"),
    path("category/<slug:category>",views.blog_category,name="category_name"),
    path("search/",views.search,name="search")
]