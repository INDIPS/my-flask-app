from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Player(models.Model):
    CHARACTER_CHOICES = [
        ('farmer', 'Farmer'),
        ('student', 'Student'),
        ('worker', 'Worker'),
        ('vendor', 'Vendor'),
        ('teacher', 'Teacher'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    character_type = models.CharField(max_length=20, choices=CHARACTER_CHOICES, default='student')
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=0)
    total_kills = models.IntegerField(default=0)
    total_deaths = models.IntegerField(default=0)
    total_matches = models.IntegerField(default=0)
    win_count = models.IntegerField(default=0)
    highest_kill_streak = models.IntegerField(default=0)
    total_damage_dealt = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-total_kills']

    def __str__(self):
        return f"{self.user.username} ({self.character_type})"

    @property
    def kill_death_ratio(self):
        if self.total_deaths == 0:
            return self.total_kills
        return round(self.total_kills / self.total_deaths, 2)

    @property
    def win_rate(self):
        if self.total_matches == 0:
            return 0
        return round((self.win_count / self.total_matches) * 100, 2)


class Match(models.Model):
    STATUS_CHOICES = [
        ('waiting', 'Waiting'),
        ('active', 'Active'),
        ('ended', 'Ended'),
    ]

    game_mode = models.CharField(max_length=20, default='solo')  # solo, duo, squad
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='waiting')
    max_players = models.IntegerField(default=100)
    current_players = models.IntegerField(default=0)
    duration = models.IntegerField(default=900)  # seconds
    started_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    winner = models.ForeignKey(Player, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Match {self.id} ({self.status})"

    def start(self):
        self.status = 'active'
        self.started_at = timezone.now()
        self.save()

    def end(self, winner_id=None):
        self.status = 'ended'
        self.ended_at = timezone.now()
        if winner_id:
            self.winner_id = winner_id
        self.save()


class MatchPlayer(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='players')
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    kills = models.IntegerField(default=0)
    deaths = models.IntegerField(default=0)
    damage_dealt = models.IntegerField(default=0)
    damage_taken = models.IntegerField(default=0)
    placed_at = models.IntegerField(null=True, blank=True)  # Placement (1st, 2nd, etc.)
    elimination_time = models.IntegerField(null=True, blank=True)  # When eliminated (seconds)
    joined_at = models.DateTimeField(auto_now_add=True)
    left_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('match', 'player')

    def __str__(self):
        return f"{self.player.user.username} in Match {self.match.id}"


class PlayerStats(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE, related_name='stats')
    matches_played_today = models.IntegerField(default=0)
    kills_today = models.IntegerField(default=0)
    total_playtime = models.IntegerField(default=0)  # seconds
    last_match_date = models.DateField(null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Stats for {self.player.user.username}"


class Weapon(models.Model):
    WEAPON_CHOICES = [
        ('cricket_bat', 'Cricket Bat'),
        ('chappal', 'Chappal'),
        ('lathi', 'Lathi'),
        ('revolver', 'Revolver'),
        ('rifle', 'Rifle'),
        ('shotgun', 'Shotgun'),
        ('bow', 'Bow'),
    ]

    name = models.CharField(max_length=20, choices=WEAPON_CHOICES, unique=True)
    damage = models.IntegerField()
    fire_rate = models.FloatField()
    magazine_size = models.IntegerField()
    range = models.IntegerField()
    rarity = models.CharField(max_length=20, default='common')  # common, rare, epic, legendary

    def __str__(self):
        return self.name


class Item(models.Model):
    ITEM_CHOICES = [
        ('medkit', 'Medical Kit'),
        ('shield', 'Shield Potion'),
        ('ammo', 'Ammunition'),
        ('grenade', 'Grenade'),
    ]

    name = models.CharField(max_length=20, choices=ITEM_CHOICES)
    effect = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    rarity = models.CharField(max_length=20, default='common')

    def __str__(self):
        return self.name
