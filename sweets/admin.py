from django.contrib import admin
from .models import Scoops, Bags, Stickers

# Register your models here.


class ScoopsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'is_vegetarian',
    )


class BagsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'weight',
        'price',
    )


class StickersAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
    )


admin.site.register(Scoops, ScoopsAdmin)
admin.site.register(Bags, BagsAdmin)
admin.site.register(Stickers, StickersAdmin)
