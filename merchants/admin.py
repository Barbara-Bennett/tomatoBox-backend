from django.contrib import admin
from .models import Merchant, MerchantTransaction

admin.site.register(Merchant)
admin.site.register(MerchantTransaction)