from django.contrib.auth.models import User
from rest_framework import permissions, viewsets

from .models import Activity, LeaderboardEntry, Team, WorkoutSuggestion
from .serializers import (
    ActivitySerializer,
    LeaderboardEntrySerializer,
    TeamSerializer,
    UserSerializer,
    WorkoutSuggestionSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('name')
    serializer_class = TeamSerializer
    permission_classes = [permissions.AllowAny]


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all().order_by('-completed_at')
    serializer_class = ActivitySerializer
    permission_classes = [permissions.AllowAny]


class LeaderboardEntryViewSet(viewsets.ModelViewSet):
    queryset = LeaderboardEntry.objects.all().order_by('rank', '-points')
    serializer_class = LeaderboardEntrySerializer
    permission_classes = [permissions.AllowAny]


class WorkoutSuggestionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSuggestion.objects.all().order_by('fitness_level', 'title')
    serializer_class = WorkoutSuggestionSerializer
    permission_classes = [permissions.AllowAny]
