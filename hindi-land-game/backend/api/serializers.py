from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Player, Match, MatchPlayer, PlayerStats, Weapon, Item

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class PlayerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    kill_death_ratio = serializers.SerializerMethodField()
    win_rate = serializers.SerializerMethodField()

    class Meta:
        model = Player
        fields = [
            'id',
            'user',
            'character_type',
            'level',
            'experience',
            'total_kills',
            'total_deaths',
            'total_matches',
            'win_count',
            'kill_death_ratio',
            'win_rate',
            'highest_kill_streak',
            'total_damage_dealt',
            'created_at',
            'updated_at',
        ]

    def get_kill_death_ratio(self, obj):
        return obj.kill_death_ratio

    def get_win_rate(self, obj):
        return obj.win_rate


class PlayerStatsSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)

    class Meta:
        model = PlayerStats
        fields = ['player', 'matches_played_today', 'kills_today', 'total_playtime', 'last_match_date']


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ['id', 'name', 'damage', 'fire_rate', 'magazine_size', 'range', 'rarity']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'effect', 'quantity', 'rarity']


class MatchPlayerSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)

    class Meta:
        model = MatchPlayer
        fields = [
            'id',
            'player',
            'kills',
            'deaths',
            'damage_dealt',
            'damage_taken',
            'placed_at',
            'elimination_time',
        ]


class MatchSerializer(serializers.ModelSerializer):
    players = MatchPlayerSerializer(many=True, read_only=True)
    winner = PlayerSerializer(read_only=True)

    class Meta:
        model = Match
        fields = [
            'id',
            'game_mode',
            'status',
            'max_players',
            'current_players',
            'duration',
            'started_at',
            'ended_at',
            'winner',
            'players',
            'created_at',
        ]


class LeaderboardSerializer(serializers.ModelSerializer):
    rank = serializers.SerializerMethodField()
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Player
        fields = [
            'rank',
            'user_username',
            'total_kills',
            'total_deaths',
            'win_count',
            'total_matches',
            'kill_death_ratio',
            'win_rate',
        ]

    def get_rank(self, obj):
        # This will be computed in the view
        return None
