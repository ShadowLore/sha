from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=60)
    intro = models.CharField('Анонс', max_length=256)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
