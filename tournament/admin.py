# tournament/admin.py
from django.contrib import admin
from .models import Player, Tournament, News, Message, AdminProfile

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'role', 'availability', 'created_at']
    list_filter = ['role', 'availability']
    search_fields = ['name', 'specialty']

@admin.register(Tournament)
class TournamentAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'location', 'created_at']
    list_filter = ['date']
    search_fields = ['name', 'location']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'content']

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['sender', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']

admin.site.register(AdminProfile)