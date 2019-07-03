from .models import Stock, Timefeed
from django.shortcuts import render
from datetime import datetime, date, time, timedelta
from django.utils import timezone
from django.views.generic import ListView


# Stocks view list for rendering 3 components: table, pagination, template
class StockList(ListView):

    model = Stock
    paginate_by = 60
    context_object_name = 'stocks'

    def get_queryset(self):
        return Stock.objects.all().order_by("-timestamp", "stock_name")

    def get_template_names(self):
        if self.request.is_ajax():
            if self.request.GET.get('pagination'):
                return ['pagination.html']
            else:
                return ['table.html']
        return ['stock.html']
