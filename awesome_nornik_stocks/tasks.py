from __future__ import absolute_import, unicode_literals
from celery import task
from .models import Stock, Timefeed
from yahoo_fin import stock_info as si


@task(bind=True)
def get_and_save_stocks(self):
    """
    Task for getting through request yahoo stocks
    """
    STOCK_LIST = ['amzn', 'nflx', 'aapl', 'goog', 'tsla', 'fb']
    stocks = [
        {
            'stock_price': si.get_live_price(stock),
            'stock_name': stock
        }
        for stock in STOCK_LIST]
    print(stocks)
    timeline = Timefeed.objects.create()

    for stock in stocks:
        entry = Stock(**stock, timestamp=timeline)
        entry.save()
