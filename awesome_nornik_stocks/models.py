from django.db import models
import django


# Timeline for stocks
class Timefeed(models.Model):
    timestamp = models.DateTimeField(('Дата'), default=django.utils.timezone.now)

    class Meta:
        verbose_name_plural = 'Stock timeline'

    def __str__(self):
        return self.timestamp.strftime("%d.%m.%Y %H:%M")


# Main stocks model with attrs
class Stock(models.Model):

    stock_name = models.CharField(('Компания'), max_length=64)
    stock_price = models.DecimalField(('Цена акции'), max_digits=9, decimal_places=2)
    timestamp = models.ForeignKey(Timefeed, related_name='stock_time', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Stocks'

    def __str__(self):
        return str('Компания: {}, Акция: {}'.format(self.stock_name, self.stock_price))
