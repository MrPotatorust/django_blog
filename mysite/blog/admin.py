from django.contrib import admin
from .models import Blogpost


# Register your models here.


class BlogpostAdmin(admin.ModelAdmin):

    list_display = ['blog_heading', 'pub_date']

    fieldsets = [
        (None, {'fields': ['blog_heading', 'pub_date']}),
        ('Text', {'fields': ['blog_text']})
    ]

admin.site.register(Blogpost, BlogpostAdmin)