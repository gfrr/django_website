from django.contrib import admin

from .models import Item, Question





class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['item_title', 'item_text', 'item_url']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

admin.site.register(Item, ItemAdmin)
admin.site.register(Question)
