from django.contrib import admin
from .models import Landmark, Comment, Photo

admin.site.register(Landmark)

admin.site.register(Photo)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('landmark', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('body',)


