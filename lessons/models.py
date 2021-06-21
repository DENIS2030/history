from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):

    title = models.CharField(max_length=255,verbose_name = "Название категории")
    description = models.TextField(verbose_name = "Описание категории")
    image = models.ImageField(verbose_name = "Изображение для категории", upload_to="lessons/")

    def __str__(self):
        return self.title

class ElectiveCategory(models.Model):

    title = models.CharField(max_length=255,verbose_name = "Название категории")
    description = models.TextField(verbose_name = "Описание категории")

    def __str__(self):
        return self.title

class Age(models.Model):
    name = models.CharField(max_length=255,verbose_name="Класс")

    def __str__(self):
        return self.name

class Books(models.Model):

    title = models.CharField(max_length=255,verbose_name = "Название Учебника")
    image = models.ImageField(verbose_name = "Изображение для категории", upload_to="books/")
    bookurl = models.TextField(
        verbose_name="Ссылка на учебник", null=True,blank=True)

    def __str__(self):
        return self.title

class Lesson(models.Model):

    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name = "Категория")
    age = models.ForeignKey(Age,on_delete=models.CASCADE,verbose_name = "Класс")
    book = models.ForeignKey(Books,on_delete=models.CASCADE,verbose_name = "Книга")
    title = models.CharField(max_length=255,verbose_name = "Название урока")
    presentation = models.TextField(verbose_name = "Ссылка на презентацию",null=True,blank=True)
    image = models.ImageField(verbose_name = "Изображение для категории", upload_to="lessons/")
    url = models.SlugField(max_length=130,unique=True)
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("lesson_detail",kwargs={"slug":self.url})
    
    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

class Pharagraph(models.Model):

    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="Урок")
    text = models.TextField(verbose_name="Текст урока")


class PharagraphImage(models.Model):

    pharagraph = models.ForeignKey(
        Pharagraph, on_delete=models.CASCADE, verbose_name="Урок")
    image = models.ImageField(
        verbose_name="Изображение для категории", upload_to="lessons/")


class AdditionalInfo(models.Model):

    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="Урок")
    text = models.TextField(verbose_name="Текст урока", null=True,blank=True)
    video = models.TextField(
        verbose_name="Ссылка на видео", null=True,blank=True)

class LearnApps(models.Model):
    lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="Урок")
    quest = models.TextField(
        verbose_name="Ссылка на задание")
    

class Elective(models.Model):
    category = models.ForeignKey(
        ElectiveCategory, on_delete=models.CASCADE, verbose_name="Категория")
    text = models.TextField(verbose_name="Текст")
    url = models.SlugField(max_length=130,unique=True)

    def get_absolute_url(self):
        return reverse("elective_detail",kwargs={"slug":self.url})
    
    def get_category(self):
        return self.category

class Multimedia(models.Model):

    description = models.TextField(verbose_name="Описание")
    multimedia = models.TextField(
        verbose_name="Ссылка на видео", null=True,blank=True)
    elective = models.ForeignKey(Elective,verbose_name="Факультатив",on_delete = models.CASCADE)


class Gallery(models.Model):
    elective = models.ForeignKey(
        Elective, on_delete=models.CASCADE, verbose_name="Категория")
    image = models.ImageField(
        verbose_name="Изображение для категории", upload_to="gallery/")
    check = models.BooleanField(default=False)
    user = models.CharField(max_length=255,verbose_name="Имя пользователя")


class Reviews(models.Model):
    """Коментарий"""
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, null=True, blank=True
    )
    lesson = models.ForeignKey(
        Lesson, verbose_name="фильм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}-{self.lesson}"

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарий"

