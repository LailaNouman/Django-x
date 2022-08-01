from django.contrib import admin

from .models import Snack

# Register your models here.

class CustomSnackAdmin(admin.ModelAdmin):
    model = Snack
    fieldsets = (
        ('Owner', {
            'fields': ('purchaser',)
        }),
        ('Snack Info', {
            'fields': (
                'name',
                'description'
            )
        })
    )

    list_display = ('name', 'purchaser')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')

admin.site.register(Snack, CustomSnackAdmin)