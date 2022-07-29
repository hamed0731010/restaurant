from django.db import models
from django.utils.translation import gettext as gt
# Create your models here.
class reservation(models.Model):
        name = models.CharField(gt("نام"),max_length=100, default=None)
        email=models.EmailField(gt("ایمیل"),default="mail@gmail.com" )
        phone_number=models.CharField(gt("شماره تماس"),max_length=11,default=None)
        number = models.IntegerField(gt("تعداد"), default=None)
        time = models.TimeField(gt("زمان رزرو"), default=None)
        date = models.DateField(gt("تاریخ رزرو"), default=None)


        def __str__(self):
            return self.name