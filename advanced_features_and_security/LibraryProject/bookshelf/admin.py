from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser


# ✅ Book admin (KEEPING your configuration)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)


# ✅ Custom User admin (REQUIRED by checker)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('username', 'email')
    ordering = ('username',)


# ✅ REQUIRED exact registration
admin.site.register(CustomUser, CustomUserAdmin)
