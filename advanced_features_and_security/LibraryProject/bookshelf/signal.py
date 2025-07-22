from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    # Optional: only run for your app
    if sender.name != 'bookshelf':
        return

    content_type = ContentType.objects.get_for_model(Book)

    permissions = {
        'can_view_books': Permission.objects.get_or_create(
            codename='can_view_books',
            name='Can view books',
            content_type=content_type
        )[0],
        'can_add_books': Permission.objects.get_or_create(
            codename='can_add_books',
            name='Can add books',
            content_type=content_type
        )[0],
        'can_edit_books': Permission.objects.get_or_create(
            codename='can_edit_books',
            name='Can edit books',
            content_type=content_type
        )[0],
        'can_delete_books': Permission.objects.get_or_create(
            codename='can_delete_books',
            name='Can delete books',
            content_type=content_type
        )[0],
    }

    group_permissions = {
        'Viewers': ['can_view_books'],
        'Editors': ['can_view_books', 'can_add_books', 'can_edit_books'],
        'Admins': ['can_view_books', 'can_add_books', 'can_edit_books', 'can_delete_books'],
    }

    for group_name, perm_codes in group_permissions.items():
        group, _ = Group.objects.get_or_create(name=group_name)
        group.permissions.set([permissions[code] for code in perm_codes])
