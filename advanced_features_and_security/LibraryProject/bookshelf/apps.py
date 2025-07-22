from django.apps import AppConfig

class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

    def ready(self):
        from .models import Book
        from django.contrib.auth.models import Group, Permission
        from django.contrib.contenttypes.models import ContentType
        

        content_type = ContentType.objects.get_for_model(Book)

        permissions = {
            'can_view_books': Permission.objects.get_or_create(codename='can_view_books', name='Can view books', content_type=content_type)[0],
            'can_add_books': Permission.objects.get_or_create(codename='can_add_books', name='Can add books', content_type=content_type)[0],
            'can_edit_books': Permission.objects.get_or_create(codename='can_edit_books', name='Can edit books', content_type=content_type)[0],
            'can_delete_books': Permission.objects.get_or_create(codename='can_delete_books', name='Can delete books', content_type=content_type)[0],
        }

        group_permissions = {
            'Viewers': ['can_view_books'],
            'Editors': ['can_view_books', 'can_add_books', 'can_edit_books'],
            'Admins': ['can_view_books', 'can_add_books', 'can_edit_books', 'can_delete_books'],
        }

        for group_name, perm_codes in group_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            group.permissions.set([permissions[code] for code in perm_codes])
