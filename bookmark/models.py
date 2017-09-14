from django.db import models

# Create your models here.
class Bookmark(models.Model):
    title = models.CharField(max_length = 100, blank = True, null = True)
    #blank 공백이라도 있는것 null = 데이터가 없는것
    url = models.URLField('url', unique=True)

    def __str__(self):
        return self.title
    #print 되는 값이 타이틀 값으로 나오게 됨

