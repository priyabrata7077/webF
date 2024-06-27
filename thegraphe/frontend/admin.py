from django.contrib import admin
from .models import *

class sizes(admin.TabularInline):
    model = size 
class ProductImages(admin.TabularInline):
    model = ProductImage 
class styles(admin.TabularInline):
    model = style
class ProductAdmin(admin.ModelAdmin):
    inlines = [sizes, styles, ProductImages]
admin.site.register(Product,ProductAdmin)
admin.site.register(CulturalSegregation)
admin.site.register(Slider)
admin.site.register(Section)
admin.site.register(sub_category)
admin.site.register(main_category)
admin.site.register(sup_category)
admin.site.register(Coupon_Code)
admin.site.register(Checkout)
admin.site.register(Additional_Information)
admin.site.register(style)
admin.site.register(size)
admin.site.register(Theme)
admin.site.register(custome)
admin.site.register(Monograms)
admin.site.register(ProductType)
admin.site.register(WeddingType)
admin.site.register(Duration)
admin.site.register(Format)
admin.site.register(UserProfile)
admin.site.register(Order)
admin.site.register(rsvp_order)
admin.site.register(notifications)
admin.site.register(Testimonial)
admin.site.register(Profile)