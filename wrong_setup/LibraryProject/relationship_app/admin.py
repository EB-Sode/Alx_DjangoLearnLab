from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author, Book, Library, Librarian, CustomUserManager, CustomUser

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'date_of_birth', 'profile_photo')}),
    )
    list_display = ['username', 'email', 'role', 'date_of_birth', 'is_staff']
    search_fields = ['username', 'email', 'role']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(CustomUserManager)
admin.site.register(CustomUser, CustomUserAdmin)
