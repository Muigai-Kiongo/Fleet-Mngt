from django.contrib import admin
from .models import MpesaTransaction


@admin.register(MpesaTransaction)
class MpesaTransactionAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'booking', 'amount', 'status', 'receipt_number', 'created_at')
    list_filter = ('status',)
    search_fields = ('phone_number', 'receipt_number', 'checkout_request_id')
    readonly_fields = ('checkout_request_id', 'created_at')