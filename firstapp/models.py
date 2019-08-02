from django.db import models


class Имя(models.Model):
    Название = models.CharField(max_length=20)

class Телефон(models.Model):
    Название = models.CharField(max_length=20)

class Комментарий(models.Model):
    Название = models.TextField()

