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
    business_type=models.CharField(max_length=100,default='Physical')
    address=models.TextField()
    address_proof=models.ImageField(upload_to='customer/address_proof/')
    id_proof=models.ImageField(upload_to='customer/id_proof/')
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
    customer_pic=models.ImageField(upload_to='customer/image/')
    ornament_pic=models.ImageField(upload_to='ornament_pic/image/')
    ornament_type=models.CharField(max_length=100)
    status=models.CharField(max_length=50,default='Pending',choices=(('Pending','Pending'),('Aproved','Aproved'),('Reject','Reject')))
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    users=models.ForeignKey(User,related_name='users',on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class ReleaseCustomer(models.Model):
    cus_name=models.CharField(max_length=50)
    mobile_number=models.CharField(max_length=15)
    business_type=models.CharField(max_length=100,default='Release')
    address=models.TextField()
    address_pic=models.ImageField(upload_to='release/image/')
    id_proof=models.ImageField(upload_to='release/id_proof/')
    pledge_slip=models.ImageField(upload_to='release/slip/')
    release_slip=models.ImageField(upload_to='release_slip/')
    release_amount=models.ImageField(upload_to='release_amount/')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.cus_name


class Wallet(models.Model):

    """This model is used to store balance of agents"""

    user=models.ForeignKey(User,related_name='wallets',on_delete=models.CASCADE)
    wallet=models.FloatField()

def generate_gold_id():
    try:
        obj=GoldPrice.objects.all().last()
        if obj is not None:
            return (obj.gold_id)+1
        else:
            return 1001
    except Exception as e:
        print(e)

class GoldPrice(models.Model):
    gold_id=models.IntegerField(default=generate_gold_id,primary_key=True,editable=False)
    price=models.FloatField()

