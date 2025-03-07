from django.db import models
from django.core.exceptions import ValidationError


class SiteSettings(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок сайта", default="")
    description = models.TextField(verbose_name="Описание сайта", default="")
    phone = models.CharField(max_length=20, verbose_name="Телефон", default="")
    phone_moderate = models.CharField(max_length=20, verbose_name="Телефон (модерация)", default="")
    city = models.CharField(max_length=255, verbose_name="Город", default="")
    street = models.CharField(max_length=255, verbose_name="Улица", default="")
    work_time = models.CharField(max_length=255, verbose_name="Рабочее время", default="")
    is_moderate = models.BooleanField(default=False, verbose_name="Сайт на модерации?")

    def save(self, *args, **kwargs):
        # Проверяем, существует ли уже запись
        if not self.pk and SiteSettings.objects.exists():
            raise ValidationError("Может существовать только одна запись настроек")
        return super().save(*args, **kwargs)

    def __str__(self):
        return 'Общие настройки сайта'

    class Meta:
        verbose_name = "Настройки сайта"
        verbose_name_plural = "Настройки сайта"


class Gift(models.Model):
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')
    title = models.CharField(max_length=255, verbose_name="Заголовок", default="")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = "Подарок"
        verbose_name_plural = "Подарки"


class FirstScreenSettings(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок", default="")
    location = models.CharField(max_length=255, verbose_name="Место", default="")
    subtitle = models.CharField(max_length=255, verbose_name="Подзаголовок", default="")
    employee_experience = models.IntegerField(verbose_name="С какого года работает?", default="")
    employee_profession = models.CharField(max_length=255, verbose_name="Специальность", default="")
    employee_fio = models.CharField(max_length=255, verbose_name="ФИО врача", default="")
    service_1_title = models.CharField(max_length=255, verbose_name="Заголовок услуги 1", default="")
    service_1_old_price = models.CharField(max_length=255, verbose_name="Старая цена услуги 1", default="")
    service_1_new_price = models.CharField(max_length=255, verbose_name="Новая цена услуги 1", default="")
    service_2_title = models.CharField(max_length=255, verbose_name="Заголовок услуги 2", default="")
    service_2_old_price = models.CharField(max_length=255, verbose_name="Старая цена услуги 2", default="")
    service_2_new_price = models.CharField(max_length=255, verbose_name="Новая цена услуги 2", default="")
    gifts_title = models.CharField(max_length=255, verbose_name="Заголовок блока", default="")
    gifts = models.ManyToManyField(Gift, verbose_name="Подарки (выберите 1 и более)", related_name='gifts')

    def save(self, *args, **kwargs):
        if not self.pk and FirstScreenSettings.objects.exists():
            raise ValidationError("Может существовать только одна запись настроек")
        return super().save(*args, **kwargs)

    def __str__(self):
        return 'Настройки первого экрана'

    class Meta:
        verbose_name = "Первый экран"
        verbose_name_plural = "Первый экран"