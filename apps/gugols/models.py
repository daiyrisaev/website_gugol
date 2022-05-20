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



# class SignIn(models.Model):
#     STATUS_NEW = "new"
#     STATUS_CONFIRMED = "confirmed"
#     STATUS_FINISHED = "finished"
#     STATUS_REJECTED = "rejected"
#     BOOKING_STATUSES = (
#         (STATUS_NEW,"Новый"),
#         (STATUS_CONFIRMED,"Подтвержден"),
#         (STATUS_FINISHED,"Завершен" ),
#         (STATUS_REJECTED,"Отменен")
#     )
#     #
#
#     category = models.ForeignKey(to=Category,on_delete=models.CASCADE)
#     mobile = models.CharField("Номер телефона",max_length=11,choices=BOOKING_STATUSES,default=STATUS_NEW)
#     is_paid = models.BooleanField("оплачено",default=False)
#     status = models.CharField("статус",max_length=11)
#
#     class Meta:
#         verbose_name= "Запищуваищий "
#         verbose_name_plural="записатся"
#
#
#     def __str__(self):
#         return f"Бронь{self.id}"


