from django.contrib import admin
from .models import Client, Item, Order


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(count=0)


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'registration_date']
    ordering = ['name', 'email']

    search_fields = ['name']
    search_help_text = 'Поиск клиента по имени'

    fields = ['name', 'address', 'phone_number', 'email', 'registration_date']

    readonly_fields = ['registration_date']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'count']
    ordering = ['id']
    list_filter = ['price', 'name']

    search_fields = ['name']
    search_help_text = 'Поиск по названию товара'

    actions = [reset_quantity]

    readonly_fields = ['add_date']

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Подробное описание',
                'fields': ['description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'count'],
            }
        ),
        (
            'Прочее',
            {
                'description': 'Фотография товара',
                'fields': ['picture'],
            }
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_name', 'total_price', 'date_ordered']
    ordering = ['id']
    list_filter = ['date_ordered', 'total_price']

    search_fields = ['id']
    search_help_text = 'Поиск по номеру заказа (id)'

    readonly_fields = ['date_ordered']


    def client_name(self, obj):
        return obj.customer.name


admin.site.register(Client, ClientAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
