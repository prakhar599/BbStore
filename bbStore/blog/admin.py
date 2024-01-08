from django.contrib import admin
from .models import Author , Blog, ContactMessage, UserFollowing
from ckeditor.widgets import CKEditorWidget
from django.db import models


class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()},
    }

admin.site.register(Author)
admin.site.register(Blog, BlogAdmin)
admin.site.register(ContactMessage)
admin.site.register(UserFollowing)


