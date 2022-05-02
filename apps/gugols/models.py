from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class Publication(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='publication_images',null=True)
    created_at = models.DateTimeField(auto_now=True)
    update=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "публикации"

    def __str__(self):
        return self.name


class OurWork(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='publication_images',null=True)

    class Meta:
        verbose_name = "Наши работы"
        verbose_name_plural = "Наши работы"

    def __str__(self):
        return self.name


class SendUserAdmin(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    message = models.TextField()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.name


class Workers(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='expert_images',null=True)

    class Meta:
        verbose_name = "Наши экперты"
        verbose_name_plural = "Наши экперты"

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='service_images',null=True)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name


class SignIn(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    category = models.ForeignKey(to=Category,on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=11)
    message = models.TextField()

    class Meta:
        verbose_name = "Записываюший человек"
        verbose_name_plural = "Записываюший человеки"

    def __str__(self):
        return self.last_name

#
# class Comment(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField(unique=True)
#     message = models.TextField()
#     amount = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)