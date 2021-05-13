from django.db import models


# Create your models here.

class DayRechargeUserAmount(models.Model):
    create_date = models.CharField(max_length=50)
    recharge_user_num = models.IntegerField()
    recharge_amount_num = models.IntegerField()

