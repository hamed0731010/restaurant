from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext as gt
from ckeditor.fields import RichTextField
# Create your models here.
class   blog(models.Model):
        name = models.CharField(gt("نام مقاله"),max_length=100, default=None)
        description = models.CharField(gt("توضیحات"), max_length=100, default=None)
        content = RichTextField(blank=False,null=False)
        author = models.ForeignKey(User,verbose_name=gt("نویسنده"), on_delete=models.CASCADE)
        pub_date = models.DateTimeField(gt("تاریخ انتشار"), default=timezone.now)
        photo = models.ImageField(gt("تصویر"), upload_to="blog/", default=None)
        category=models.ForeignKey("category",related_name="blog",verbose_name="دسته بندی" ,on_delete=models.CASCADE,null=True,blank=True )
        tag=models.ManyToManyField("tag",related_name="blogs",verbose_name="تگ")
        def __str__(self):
                return self.name
class category(models.Model):
        title=models.CharField(gt("نام دسته بندی"),max_length=30)
        slug=models.SlugField(gt("نامک"))
        date=models.DateTimeField(gt("تاریخ انتشار"),auto_now=False,auto_now_add=True)
        def __str__(self):
                return self.title
class tag(models.Model):
        title=models.CharField(gt("نام تگ"),max_length=30)
        slug=models.SlugField(gt("نامک"))
        date=models.DateTimeField(gt("تاریخ انتشار"),auto_now=False,auto_now_add=True)
        def __str__(self):
                return self.title
class comments(models.Model):
        blog=models.ForeignKey("blog",related_name="blog",verbose_name="بلاگ" ,on_delete=models.CASCADE,null=True,blank=True)
        name=models.CharField(gt("نام "),max_length=30)
        email=models.EmailField(gt("ایمیل"),default="mail@gmail.com" )
        message=models.TextField(gt("نظر"))
        date=models.DateTimeField(gt("تاریخ انتشار"),auto_now=False,auto_now_add=True)

        def __str__(self):
                return self.email
