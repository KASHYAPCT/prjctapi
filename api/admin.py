from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Detials)
admin.site.register(Cars)
admin.site.register(Category)
admin.site.register(ProductVariant)
admin.site.register(CarVariant)
admin.site.register(BlackListedToken)