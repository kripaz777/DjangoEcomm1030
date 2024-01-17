from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Ad)
admin.site.register(Slider)
admin.site.register(Brand)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","category","brand","label","stock","price","discounted_price")
    list_filter = ("category","brand","label","stock" )
    search_fields = ("name","description")
    # fields = ("price","discounted_price")
    ordering = ("name", "category", "brand", "stock", "price")

    # class Meta:

admin.site.register(Contact)
admin.site.register(ContactInfo)
admin.site.register(ProductReview)
admin.site.register(Cart)