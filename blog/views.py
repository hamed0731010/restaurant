from django.shortcuts import render
from .models import blog,tag,category,comments
from .forms import CommentForm
from django.core.paginator import Paginator
# Create your views here.
def blog_list(request):
    blog_list=blog.objects.all()
    paginator = Paginator(blog_list, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        "blogs":page_obj
    }
    return  render(request,"blog/blog.html",context)
def blog_detail(requset,id):
    blog_detail=blog.objects.get(id=id)
    tags = tag.objects.all().filter(blogs=blog_detail)   #?????
    rencent=blog.objects.all().order_by("pub_date")[:3]
    categories=category.objects.all()
    comment=comments.objects.all().filter(blog=blog_detail)
    if requset.method=="POST":
        form=CommentForm(requset.POST)
        if form.is_valid():
            new_name=form.cleaned_data['name']
            new_email=form.cleaned_data['email']
            new_message=form.cleaned_data['message']
            new_comment=comments(blog=blog_detail,name=new_name,email=new_email,message=new_message)
            new_comment.save()

    context={
              "detail_blogs":blog_detail,
                "tags": tags,
                "recents" : rencent,
                "category" :categories,
                "comments" : comment
            }
    return render(requset,"blog/blog-details.html",context)
def blog_tag(request,tag):
    blog_list = blog.objects.filter(tag__slug=tag)

    context = {
        "blogs": blog_list
    }
    return render(request, "blog/blog.html", context)

def blog_category(request,category):
    blog_list = blog.objects.filter(category__slug=category)

    context = {
        "blogs": blog_list
    }
    return render(request, "blog/blog.html", context)
def search(request):
    if request.method == "GET":
        q=request.GET.get("search")
    blog_list=blog.objects.filter(content__icontains=q)
    context={"blog_list":blog_list}
    return render(request,"blog/blog.html",context)