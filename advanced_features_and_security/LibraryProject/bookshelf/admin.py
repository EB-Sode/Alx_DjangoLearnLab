from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import Author, Library, Librarian, CustomUser

# Register your models here.

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

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Author)
admin.site.register(Library)
admin.site.register(Librarian)



