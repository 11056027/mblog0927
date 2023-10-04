from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200) #字元長度
    slug = models.CharField(max_length=200)
    body = models.TextField() #不限制長度
    pub_date = models.DateTimeField(auto_now_add=True) #auto_now自動取得現在時間
    
    class Meta:
        ordering = ('-pub_date',) #ordering用-pub_date做排序
        
    def __str__(self) -> str:
        return self.title