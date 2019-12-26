from django.contrib import admin
from .models import Landmark, Comment, ProposedLandmark

admin.site.register(Landmark)
admin.site.register(ProposedLandmark)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('landmark', 'created', 'active')
    list_filter = ('active', 'created')
    search_fields = ('body',)


