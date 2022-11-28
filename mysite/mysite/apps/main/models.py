from django.db import models


#Модель последних новостей
class LatestNewsModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)


