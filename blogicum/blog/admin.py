# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from blog.models import Category, Location, Post

# admin.site.register(Category)
# admin.site.register(Location)
# admin.site.register(Post)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at')
    list_editable = ('is_published',)  # Что можно редактировать прямо в списке
    search_fields = ('title',)  # По каким полям можно искать
    list_filter = ('is_published',)  # Фильтры справа


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('name',)
    list_filter = ('is_published',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author', 'is_published')
    list_editable = ('is_published',)
    search_fields = ('title', 'text')
    list_filter = ('category', 'is_published')
    date_hierarchy = 'pub_date'  # Навигация по датам
