from django.db import models

class Artiles(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Описание')
    date = models.DateTimeField('Дата публикации')
    image = models.ImageField('Изображение', upload_to='articles/images/', null=True, blank=True)

    def __str__(self):
        return self.title

