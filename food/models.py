from django.db import models
from django.utils.translation import gettext as gt
# Create your models here.
class food(models.Model):
        food_type=[
                ("cake","کیک"),("lunch","ناهار"),("coffee","قهوه"),("drink","نوشیدنی سرد")
        ]
        name=models.CharField(max_length=100,default=None)
        description=models.CharField(gt("توضیحات"),max_length=30,default=None)
        rate=models.IntegerField(gt("امتیاز"),default=None)
        price=models.IntegerField(gt("قیمت"),default=None)
        time=models.IntegerField(gt("زمان"),default=None)
        pub_date=models.DateTimeField(gt("تاریخ انتشار"),default=None)
        photo=models.ImageField(gt("تصویر"),upload_to="foods/",default=None)
        foodtype=models.CharField(gt("نوع سفارش"),max_length=10,choices=food_type,default="drink")

        def __str__(self):
                return self.name