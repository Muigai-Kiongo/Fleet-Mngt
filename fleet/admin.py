from django.contrib import admin
from .models import Car, VehicleAssignment, ConditionReport, MechanicRequest


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'plate_number', 'daily_rate', 'is_available', 'status')
    list_filter = ('is_available', 'status', 'brand')
    search_fields = ('name', 'plate_number', 'brand')
    list_editable = ('is_available', 'status')


@admin.register(VehicleAssignment)
class VehicleAssignmentAdmin(admin.ModelAdmin):
    list_display = ('profile', 'car', 'assigned_date', 'return_date', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('profile__user__username', 'car__name')


@admin.register(ConditionReport)
class ConditionReportAdmin(admin.ModelAdmin):
    list_display = ('profile', 'car', 'reported_at')
    search_fields = ('profile__user__username', 'car__name')


@admin.register(MechanicRequest)
class MechanicRequestAdmin(admin.ModelAdmin):
    list_display = ('profile', 'car', 'status', 'requested_at', 'completed_at')
    list_filter = ('status',)
    search_fields = ('profile__user__username', 'car__name')
    list_editable = ('status',)