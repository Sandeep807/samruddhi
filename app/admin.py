from django.contrib import admin
from django.utils.html import format_html
admin.site.site_header="Samruddhi"
admin.site.index_title="Welcome to Samruddhi"
from .models import *
from django.contrib.auth.models import User
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('users','cus_id','name','mobile_number','gross_weight',
                'stone','net_weight','gold_price','purity',
                'gross_amount','margin','net_amount','releasing',
                'amount_paid','customer_pic','ornament_pic','status','created_at')

    list_filter=['status','created_at','users']
    search_fields=['mobile_number']

@admin.register(Wallet)
class UserWallet(admin.ModelAdmin):
    list_display=('user','wallet','id')


    
    # def image_tag(self, obj):
    #     return format_html('<img src="{}" />'.format(obj.customer_pic.url))

    # image_tag.short_description = 'Image'

    # list_display = ['image_tag',]
