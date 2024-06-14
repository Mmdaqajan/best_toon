from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Expense(models.Model):
    description = models.CharField(max_length=255, verbose_name='توضیحات')
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    amount = models.BigIntegerField(verbose_name='مقدار')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')

    # def __str__(self):
    #     pass

    class Meta:
        verbose_name = 'خرج'
        verbose_name_plural = 'خرج ها'
