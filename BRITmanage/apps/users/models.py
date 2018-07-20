from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.


class UserProfile(AbstractUser):
    """
    用户
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
    mobile = models.CharField(max_length=11, null=True, verbose_name="电话")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default="female", verbose_name="性别")
    email = models.EmailField(max_length=100, null=False, verbose_name="邮箱")
    q_number = models.IntegerField(null=True, verbose_name="QQ号码")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username