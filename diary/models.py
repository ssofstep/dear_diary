from django.contrib.auth.models import AbstractUser
from django.db import models

from users.models import CustomUser


class Note(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(verbose_name="Тема записки", max_length=150)
    text = models.TextField(verbose_name="Текст", blank=True, null=True)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания" ,blank=True, null=True)

    def __str__(self):
        return f'{self.title} {self.creation_date}'

    class Meta:
        verbose_name = 'Записка'
        verbose_name_plural = 'Записки'
        ordering = ['title', 'text']
