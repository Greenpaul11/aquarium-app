from django.contrib import admin
from .models import Article, Photo, Tag

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'id']
    search_fields = ['title']
    
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['description']
    search_fields = ['description']
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Tag)
