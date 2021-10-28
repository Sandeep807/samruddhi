from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    cus_id=models.AutoField(primary_key=True,editable=False)
    name=models.CharField(max_length=50)
    mobile_number=models.CharField(max_length=15)
    gross_weight=models.FloatField()
    stone=models.FloatField(default=0)
    net_weight=models.FloatField()
    gold_price=models.IntegerField()
    purity=models.IntegerField()
    gross_amount=models.FloatField()
    margin=models.FloatField()
    net_amount=models.FloatField()
    releasing=models.FloatField()
    amount_paid=models.FloatField()
    customer_pic=models.ImageField(upload_to='customer/image')
    ornament_pic=models.ImageField(upload_to='ornament_pic/image')
    status=models.CharField(max_length=50,choices=(('Aproved','Aproved'),('Reject','Reject')),null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    users=models.ForeignKey(User,related_name='users',on_delete=models.CASCADE)
    
class Wallet(models.Model):
    user=models.ForeignKey(User,related_name='wallets',on_delete=models.CASCADE)
    wallet=models.FloatField()

