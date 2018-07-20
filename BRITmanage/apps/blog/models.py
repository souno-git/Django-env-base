from django.db import models
from apps.users.models import UserProfile
from datetime import datetime
from DjangoUeditor.models import UEditorField


# Create your models here.
class BlogArt(models.Model):
    title = models.CharField(max_length=50, null=False, verbose_name="文章标题")
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="作者")
    label = models.CharField(max_length=50, verbose_name="标签")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    content = UEditorField(width="120%", height=600, toolbars='normal', imagePath="blog/images/", filePath="blog/files/", default="", verbose_name=u"文章内容")

    class Meta:
        verbose_name = "文章管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title