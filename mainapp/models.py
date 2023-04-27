from django.db import models


class UserStatus:
    blocked = 'blocked'
    active = 'active'
    waiting = 'waiting'

    CHOICES = (
        (blocked, 'blocked'),
        (active, 'active'),
        (waiting, 'waiting'),
    )


class AdStatus:
    draft = 'draft'
    moderate = 'moderate'
    rejected = 'rejected'
    withdrawn = 'withdrawn'
    active = 'active'

    CHOICES = (
        (draft, 'draft'),
        (moderate, 'moderate'),
        (rejected, 'rejected'),
        (withdrawn, 'withdrawn'),
        (active, 'active'),
    )


# Структура БД
class User(models.Model):
    """Пользователь"""
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50, null=True, blank=True)
    role = models.CharField('Роль', max_length=50)
    email = models.EmailField('Адрес электронной почты', max_length=50)
    phone = models.CharField('Номер телефона', max_length=50)
    convenient_time = models.CharField('Когда удобно принимать звонки', max_length=50)
    status_user = models.CharField(max_length=20, choices=UserStatus.CHOICES, default=UserStatus.waiting)

    def __str__(self):
        return str(self.name)


class Ad(models.Model):
    """Объявление"""
    name_ad = models.CharField('Название объявления', max_length=50)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='ID категории')
    city = models.ForeignKey('Cities', on_delete=models.CASCADE, verbose_name='ID города')
    description_ad = models.TextField('Описание объявления', blank=True)
    date_pub = models.DateField('Дата публикации')
    price = models.CharField('Стоимость', max_length=50)
    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='ID пользователя')
    number_views = models.IntegerField('Количество просмотров')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    status_ad = models.CharField(max_length=20, choices=AdStatus.CHOICES, default=AdStatus.draft)

    def __str__(self):
        return str(self.name_ad)


class Category(models.Model):
    """Категории"""
    name_cat = models.CharField('Название категории', max_length=50)
    code = models.CharField('Код', max_length=50)
    description_cat = models.TextField('Описание категории', blank=True)
    parent = models.ForeignKey('self', blank=True, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name_cat)


class Cities(models.Model):
    """Города"""
    name_city = models.CharField(max_length=50, blank=False, null=True)
    region = models.ForeignKey('Region', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name_city)


class Region(models.Model):
    """Регионы"""
    name_reg = models.CharField(max_length=50, blank=False, null=True)

    def __str__(self):
        return str(self.name_reg)


class ModerationAd(models.Model):
    """Запись о модерации объявления"""
    date_moder = models.DateField
    ad = models.ForeignKey('Ad', on_delete=models.CASCADE)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    publication = models.BooleanField(default=False)
    reason = models.TextField('Причина отклонения', blank=True, null=True)
