from __future__ import unicode_literals

from django.db import models
from datetime import date, datetime, timedelta
# class Portfolio(models.Model):
#     """
#     A portfolio belonging to a User. A portfolio has a cash balance (defaulting to $100,000),
#     stocks and transactions.
#     """
#     created = models.DateTimeField(auto_now_add=True)
#     name = models.CharField(
#         max_length=100,
#         default= "X"+str(date.today)
#     )
#     cash = models.FloatField()
#     # owner = models.ForeignKey('auth.User', related_name='portfolios')

class TransactionManager(models.Manager):
    def newTransaction(self,data):
        pass


# Create your models here.
class transaction(models.Model):
    O = 'O  '
    L = 'L  '
    S = 'S  '
    C = 'C  '
    W = 'W  '
    T = 'T  '
    POSITION_TYPE = (
        (O, 'Option'),
        (L, 'Long Position'),
        (S, 'Short Position'),
        (C, 'Commodity Position'),
        (T, 'Tracking Position'),
        (W, 'Watchlist Item')
    )
    NYSE = 'NYSE'
    AMEX = 'AMEX'
    NASDAQ = 'NASDQ'
    EXCHANGE = (
        (NYSE, 'NYSE'),
        (AMEX, 'American Stock Exchange'),
        (NASDAQ, 'Nasdaq')
    )
    exchange = models.CharField(
        max_length = 5,
        choices = EXCHANGE,
    )
    ticker = models.CharField(max_length = 45)
    cik = models.CharField(max_length = 10)
    underlying = models.CharField(max_length = 45)
    type = models.CharField(
        max_length = 3,
        choices = POSITION_TYPE,
        default = L
    )
    description = models.CharField(max_length = 100)
    quantity = models.DecimalField(max_digits = 15, decimal_places = 4)
    cost = models.DecimalField(max_digits = 15, decimal_places = 4)
    transactionDate = models.DateField(default = date.today)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
    objects = TransactionManager()
