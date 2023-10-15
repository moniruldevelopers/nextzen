from django.contrib import admin
from .models import Category, Post_list
# Register your models here.
admin.site.register(Category)

class Post_list_Admin(admin.ModelAdmin):
    list_display= ( 'page_name', 'page_link')

admin.site.register(Post_list,Post_list_Admin)