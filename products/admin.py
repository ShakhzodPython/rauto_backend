from django.contrib import admin

from .models import *


# Register your models here.

@admin.register(CarCategory)
class CarCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)


@admin.register(BodyType)
class BodyTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)


@admin.register(Gearbox)
class GearboxAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)


@admin.register(TypeFuel)
class TypeFuelAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)


@admin.register(MachineCondition)
class MachineConditionAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)


@admin.register(MachineDrive)
class MachineDriveAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('category', 'price', 'currency', 'year', 'author')
    search_fields = ('title', 'category__title', 'author__username')
