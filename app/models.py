from django.db import models

class p(models.Model):
    pass

class Rubric(models.Model):
    name = models.CharField('Имя', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural= 'Категории'
        verbose_name= 'Создать Категорию'
        ordering = ['name']



class Post(models.Model):
    title = models.CharField('Название', max_length=30, blank=True, null=True)
    image1 = models.ImageField('Фото 1', blank=True, null=True)
    image2 = models.ImageField('Фото 2', blank=True, null=True)
    image3 = models.ImageField('Фото 3', blank=True, null=True)
    date = models.DateTimeField('Дата выпуска', auto_now_add=True, blank=True, null=True)
    inf = models.TextField('Иформация',max_length=300, blank=True, null=True)
    rubric = models.ForeignKey(Rubric, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural= 'Посты'
        verbose_name= 'Создать Пост'
        ordering = '-date',

