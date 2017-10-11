from __future__ import unicode_literals

from django.db import models
from ..userloginreg.models import User

# class PortfolioManager(models.Manager):
    # def portfolioValidator(portfolio):
    #     portfolioRow = Portfolio.objects.get(id = portfolio.id)
    #     portfolioRow.title = portfolio.title
    #     try:
    #         portfolioRow.save()
    #         return True
    #     except:
    #         return False
# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length = 70, null = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, related_name = "portfolios")
    # objects = PortfolioManager()
