from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
def generate_id():

    """This method is used to generate four digits start from 1001 sequence by"""
    
    try:
        obj=Customer.objects.all().last()
        if obj is not None:
            return (obj.cus_id)+1
        else:
            return 1001
    except Exception as e:
        print(e)

class Customer(models.Model):

    """This model is used to store data of customers"""

    cus_id=models.IntegerField(default=generate_id,primary_key=True,editable=False)
    name=models.CharField(max_length=50)
    mobile_number=models.CharField(max_length=15,unique=True)
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
    customer_pic=models.ImageField(upload_to='customer/image',null=True,blank=True)
    ornament_pic=models.ImageField(upload_to='ornament_pic/image',null=True,blank=True)
    ornament_type=models.CharField(max_length=100)
    status=models.CharField(max_length=50,default='Pending',choices=(('Pending','Pending'),('Aproved','Aproved'),('Reject','Reject')))
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    users=models.ForeignKey(User,related_name='users',on_delete=models.CASCADE)
    
class Wallet(models.Model):

    """This model is used to store balance of agents"""

    user=models.ForeignKey(User,related_name='wallets',on_delete=models.CASCADE)
    wallet=models.FloatField()

