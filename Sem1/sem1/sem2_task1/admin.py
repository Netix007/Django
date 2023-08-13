from django.contrib import admin
from .models import Author, Article


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email')
    ordering = ('surname', 'name')
    list_filter = ('name', )
    search_fields = ('name', )

    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'surname', ],
            },
        ),
        (
            'Contacts',
            {
                'classes': ['collapse'],
                'fields': ['email', ],
            }
        ),
        (
            'Bio',
            {
                'classes': ['collapse'],
                'fields': ['biography', 'birthday', ],
            }
        )
    ]


admin.site.register(Author, AuthorAdmin)
admin.site.register(Article)
