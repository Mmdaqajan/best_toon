from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    description = models.CharField(max_length=255, verbose_name='توضیحات')
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    amount = models.BigIntegerField(verbose_name='مقدار')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')

    def __str__(self):
        return '{}-{}'.format(self.date, self.amount)

    class Meta:
        verbose_name = 'خرج'
        verbose_name_plural = 'خرج ها'


class Income(models.Model):
    description = models.CharField(max_length=255, verbose_name='توضیحات')
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')
    amount = models.BigIntegerField(verbose_name='مقدار')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')

    def __str__(self):
        return '{}-{}'.format(self.date, self.amount)

    class Meta:
        verbose_name = 'درامد'
        verbose_name_plural = 'درامد ها'
