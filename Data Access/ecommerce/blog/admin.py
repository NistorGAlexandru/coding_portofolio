from django.contrib import admin
from .models import Post

# Register your models here.

# admin.site.register(Post)



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'slug']
    prepopulated_fields = {'slug':('title',)}
    search_fields = ['title']
    

