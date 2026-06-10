from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.utils import timezone
from django.db.models import Q

from api.models import Player, Match, MatchPlayer, PlayerStats, Weapon, Item
from api.serializers import (
    PlayerSerializer,
    MatchSerializer,
    LeaderboardSerializer,
    PlayerStatsSerializer,
    WeaponSerializer,
)


class HealthCheckView(APIView):
    """
    Health check endpoint for monitoring
    """
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            'status': 'healthy',
            'timestamp': timezone.now()
        })


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoints for player management
    """
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Player.objects.all()

    def get_object(self):
        try:
            return Player.objects.get(user=self.request.user)
        except Player.DoesNotExist:
            return None

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Get current player's profile"""
        try:
            player = Player.objects.get(user=request.user)
            serializer = PlayerSerializer(player)
            return Response(serializer.data)
        except Player.DoesNotExist:
            return Response({'error': 'Player not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])
    def create_profile(self, request):
        """Create a new player profile"""
        character_type = request.data.get('character_type', 'student')
        
        if Player.objects.filter(user=request.user).exists():
            return Response(
                {'error': 'Player profile already exists'},
                status=status.HTTP_400_BAD_REQUEST
            )

        player = Player.objects.create(
            user=request.user,
            character_type=character_type
        )
        PlayerStats.objects.create(player=player)
        
        serializer = PlayerSerializer(player)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def stats(self, request):
        """Get player statistics"""
        player = self.get_object()
        if not player:
            return Response({'error': 'Player not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PlayerSerializer(player)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def matches_history(self, request):
        """Get player's match history"""
        player = self.get_object()
        if not player:
            return Response({'error': 'Player not found'}, status=status.HTTP_404_NOT_FOUND)

        matches = MatchPlayer.objects.filter(player=player).order_by('-joined_at')[:20]
        data = []
        for mp in matches:
            data.append({
                'match_id': mp.match.id,
                'placement': mp.placed_at,
                'kills': mp.kills,
                'damage_dealt': mp.damage_dealt,
                'joined_at': mp.joined_at,
            })
        return Response(data)


class MatchViewSet(viewsets.ModelViewSet):
    """
    API endpoints for match management
    """
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    @action(detail=False, methods=['post'])
    def create_match(self, request):
        """Create a new match"""
        game_mode = request.data.get('game_mode', 'solo')
        
        match = Match.objects.create(
            game_mode=game_mode,
            max_players=100 if game_mode == 'solo' else (50 if game_mode == 'duo' else 25)
        )
        
        serializer = MatchSerializer(match)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def join(self, request, pk=None):
        """Join a match"""
        match = self.get_object()
        
        if match.status != 'waiting':
            return Response(
                {'error': 'Match is not accepting players'},
                status=status.HTTP_400_BAD_REQUEST
            )

        player = Player.objects.get(user=request.user)
        
        if MatchPlayer.objects.filter(match=match, player=player).exists():
            return Response(
                {'error': 'Already in match'},
                status=status.HTTP_400_BAD_REQUEST
            )

        match_player = MatchPlayer.objects.create(match=match, player=player)
        match.current_players += 1
        match.save()

        return Response(MatchSerializer(match).data)

    @action(detail=True, methods=['post'])
    def start(self, request, pk=None):
        """Start a match"""
        match = self.get_object()
        match.start()
        return Response(MatchSerializer(match).data)

    @action(detail=True, methods=['post'])
    def end(self, request, pk=None):
        """End a match and record results"""
        match = self.get_object()
        winner_id = request.data.get('winner_id')
        
        match.end(winner_id)
        
        # Update player statistics
        for mp in MatchPlayer.objects.filter(match=match):
            player = mp.player
            player.total_matches += 1
            player.total_kills += mp.kills
            player.total_deaths += mp.deaths
            player.total_damage_dealt += mp.damage_dealt
            
            if mp.placed_at == 1:
                player.win_count += 1
            
            player.save()

        return Response(MatchSerializer(match).data)

    @action(detail=True, methods=['get'])
    def leaderboard(self, request, pk=None):
        """Get leaderboard for a match"""
        match = self.get_object()
        players = MatchPlayer.objects.filter(match=match).order_by('placed_at')
        
        data = []
        for i, mp in enumerate(players, 1):
            data.append({
                'rank': i,
                'player': mp.player.user.username,
                'kills': mp.kills,
                'damage_dealt': mp.damage_dealt,
                'placement': mp.placed_at,
            })
        
        return Response(data)


class LeaderboardViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoints for leaderboard
    """
    queryset = Player.objects.all().order_by('-total_kills')
    serializer_class = LeaderboardSerializer

    def list(self, request):
        """Get global leaderboard"""
        players = Player.objects.all().order_by('-total_kills')[:100]
        
        data = []
        for i, player in enumerate(players, 1):
            serializer = LeaderboardSerializer(player)
            player_data = serializer.data
            player_data['rank'] = i
            data.append(player_data)
        
        return Response(data)

    @action(detail=False, methods=['get'])
    def by_kills(self, request):
        """Get leaderboard ordered by kills"""
        players = Player.objects.all().order_by('-total_kills')[:50]
        data = []
        for i, player in enumerate(players, 1):
            serializer = LeaderboardSerializer(player)
            player_data = serializer.data
            player_data['rank'] = i
            data.append(player_data)
        return Response(data)

    @action(detail=False, methods=['get'])
    def by_wins(self, request):
        """Get leaderboard ordered by wins"""
        players = Player.objects.all().order_by('-win_count')[:50]
        data = []
        for i, player in enumerate(players, 1):
            serializer = LeaderboardSerializer(player)
            player_data = serializer.data
            player_data['rank'] = i
            data.append(player_data)
        return Response(data)

    @action(detail=False, methods=['get'])
    def by_wins_rate(self, request):
        """Get leaderboard ordered by win rate"""
        players = Player.objects.filter(total_matches__gte=10).all()
        players = sorted(players, key=lambda x: x.win_rate, reverse=True)[:50]
        
        data = []
        for i, player in enumerate(players, 1):
            serializer = LeaderboardSerializer(player)
            player_data = serializer.data
            player_data['rank'] = i
            data.append(player_data)
        return Response(data)
