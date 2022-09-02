from django.db import models
from datetime import date


class Movie(models.Model):
    """Фильм"""
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    realise_date = models.DateField('Премьера в мире', default=date.today)

    def __str__(self):
        return self.title


class Feedback(models.Model):
    """Отзывы"""
    title = models.CharField('Название', max_length=100)
    name = models.CharField('Имя', max_length=100)
    email = models.EmailField()
    text = models.TextField('Сообщение')
    creation_date = models.DateTimeField("Дата создания")
    cinema = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.title


class showtime(models.Model):
    """Показ фильмов """
    movie = models.CharField("Название", max_length=100)
    datetime = models.DateTimeField("Дата создания")
    price = models.CharField('Цена', max_length=100)


class Cinema(models.Model):
    """Кинотеатр"""
    adress = models.CharField('Адрес', max_length=50)


class Room(models.Model):
    """Комнаты"""
    adress = models.CharField('Адрес', max_length=50)
    title = models.CharField('Название', max_length=100)

    def __str__(self):
        return self.title


class Seat(models.Model):
    """Место"""
    row = models.SmallIntegerField('Ряд', max_length=100)
    number = models.SmallIntegerField('Номер')
    room = models.CharField('Комната')


class HistoryItem(models.Model):
    """История"""
    ticket = models.CharField('Название Билета', max_length=50)
    price = models.PositiveIntegerField('Цена билета')
    user = models.CharField('Имя пользователя', max_length=50)
    buy_date = models.DateField('Дата покупки билета')


class Ticket(models.Model):
    """Билет"""
    datetime = models.DateField("Дата билета")
    buy_by = models.CharField("Кем куплен билет", max_lenght=50)
    showtime = models.DateField('Дата показа')
