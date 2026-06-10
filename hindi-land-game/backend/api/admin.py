from django.contrib import admin  # type: ignore[reportMissingImports]
from .models import Player, Match, MatchPlayer, PlayerStats, Weapon, Item

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ['user', 'character_type', 'level', 'total_kills', 'total_deaths', 'created_at']
    list_filter = ['character_type', 'level', 'created_at']
    search_fields = ['user__username', 'user__email']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ['id', 'game_mode', 'status', 'current_players', 'max_players', 'winner', 'created_at']
    list_filter = ['game_mode', 'status', 'created_at']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(MatchPlayer)
class MatchPlayerAdmin(admin.ModelAdmin):
    list_display = ['player', 'match', 'kills', 'placed_at', 'joined_at']
    list_filter = ['match', 'joined_at']
    search_fields = ['player__user__username']

@admin.register(PlayerStats)
class PlayerStatsAdmin(admin.ModelAdmin):
    list_display = ['player', 'matches_played_today', 'kills_today', 'total_playtime']
    readonly_fields = ['last_updated']

@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ['name', 'damage', 'fire_rate', 'magazine_size', 'range', 'rarity']
    list_filter = ['rarity']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'effect', 'quantity', 'rarity']
    list_filter = ['rarity']
