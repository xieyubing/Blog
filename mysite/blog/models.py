from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField


class BlogType(models.Model):
    type_name = models.CharField(u'标签', max_length=10)

    def __str__(self):
        return self.type_name


class Blog(models.Model):
    title = models.CharField(u'标题', max_length=30)
    content = UEditorField('文章', imagePath="uploadimg/", toolbars='besttome', filePath='upload/', blank=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    def profile(self):
        if len(str(self.content))>30:
            return '{}...' .format(str(self.content)[0:65])
        else:
            return str(self.content)






