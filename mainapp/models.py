from django.db import models

class File(models.Model):
    title = models.CharField('Заголовок', max_length=250)  # Название файла
    anons = models.CharField('Анонс', max_length=250, null=True)
    uploaded_file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ArtLine(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    anons = models.CharField('Анонс', max_length=200)

class Home(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    anons = models.CharField('Анонс', max_length=200)
    full_text = models.TextField('Описание')


    def __str__(self):
        return self.title
