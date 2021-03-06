from django.db import models
from django.shortcuts import reverse
from django.utils.timezone import now







class ModelNews(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(null=True, blank=True, verbose_name='Контент')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = 'Новости'
        verbose_name = 'Обьявление'
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=40, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

class Autor(models.Model):
    email = models.EmailField(null=True,blank=True)
    date = models.DateField(default=now)
    def __str__(self):
        return'%s, %s' % (self.email,self.date)
    def get_absolute_url(self):
        return reverse(args=[str(self.id)])






