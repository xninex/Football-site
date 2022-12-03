from django.db import models


#Модель последних новостей
class LatestNewsModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    content = models.TextField(verbose_name='Текст новости')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Последняя новость'
        verbose_name_plural = 'Последние новости'


#Модель комментариев
class Comment(models.Model):
    new = models.ForeignKey(LatestNewsModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='Имя комментатора')
    text = models.TextField(verbose_name='Текст комментария')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'