from django.contrib import admin
from django.utils.html import format_html
admin.site.site_header="Samruddhi"
admin.site.index_title="Welcome to Samruddhi"
from .models import *
from django.contrib.auth import get_user_model
# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('user_id','users','cus_id','name','mobile_number','business_type','address','address_proof_image',
                'id_proof_image','gross_weight','stone','net_weight','gold_price','purity',
                'gross_amount','margin','net_amount','releasing',
                'amount_paid','customer_image','ornament_image','status','created_at')

    list_filter=['created_at','users','status']
    search_fields=['mobile_number']
    list_per_page=10

    def address_proof_image(self,obj):
        return format_html(f'<img src="/media/{obj.address_proof}" style=height:50px;width:50px>')
    
    def id_proof_image(self,obj):
        return format_html(f'<img src="/media/{obj.id_proof}" style=height:50px;width:50px>')


    def customer_image(self,obj):
        return format_html(f'<img src="/media/{obj.customer_pic}" style=height:50px;width:50px>')

    def ornament_image(self,obj):
        return format_html(f'<img src="/media/{obj.ornament_pic}" style=height:50px;width:50px>')

@admin.register(ReleaseCustomer)  
class ReleaseCustomerAdmin(admin.ModelAdmin):
    list_display=['business_type','address','address_image',
                'proof_image','pledge_slip_image','release_slip_image',
                'release_amount_image','created_at']

    def address_image(self,obj):
        return format_html(f'<img src="/media/{obj.address_pic}" style=height:50px;width:50px>')

    def proof_image(self,obj):
        return format_html(f'<img src="/media/{obj.id_proof}" style=height:50px;width:50px>')

    def pledge_slip_image(self,obj):
        return format_html(f'<img src="/media/{obj.pledge_slip}" style=height:50px;width:50px>')

    def release_slip_image(self,obj):
        return format_html(f'<img src="/media/{obj.release_slip}" style=height:50px;width:50px>')

    def release_amount_image(self,obj):
        return format_html(f'<img src="/media/{obj.release_amount}" style=height:50px;width:50px>')


@admin.register(Wallet)
class UserWallet(admin.ModelAdmin):
    list_display=('user_id','wallet','id')

@admin.register(GoldPrice)
class GoldPriceAdmin(admin.ModelAdmin):
    list_display=['gold_id','price']
    # fieldsets = (
    #     ('Customer Details', {
    #         "fields": (
    #             'name','mobile_number',
    #         ),
    #     }),
    
    #     ('Gold Details', {
    #         "fields": (
    #             'gross_weight','stone',
    #              'net_weight','gold_price',
    #              'purity','gross_amount',
    #              'margin','net_amount',
    #              'releasing','amount_paid',
    #         ),
    #     }),
    
    #         ('Customer and Ornament Image', {
    #         "fields": (
    #             # 'customer_image',
    #             #'ornament_image',
    #              'status',
    #         ),
    #     }),
    # )    
    # def image_tag(self, obj):
    #     return format_html('<img src="{}" />'.format(obj.customer_pic.url))

    # image_tag.short_description = 'Image'

    # list_display = ['image_tag',]