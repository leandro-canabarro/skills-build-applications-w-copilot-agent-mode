from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    display_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    fitness_level = models.CharField(max_length=30, default='beginner')

    def __str__(self):
        return self.display_name


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(User, related_name='fitness_teams', blank=True)

    def __str__(self):
        return self.name


class Activity(models.Model):
    class ActivityType(models.TextChoices):
        RUN = 'run', 'Run'
        WALK = 'walk', 'Walk'
        STRENGTH = 'strength', 'Strength'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=20, choices=ActivityType.choices)
    duration_minutes = models.PositiveIntegerField()
    distance_km = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    points = models.PositiveIntegerField(default=0)
    completed_at = models.DateTimeField()

    class Meta:
        ordering = ['-completed_at']


class LeaderboardEntry(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='leaderboard_entry')
    points = models.PositiveIntegerField(default=0)
    rank = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['rank', '-points']


class WorkoutSuggestion(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    fitness_level = models.CharField(max_length=30)
    duration_minutes = models.PositiveIntegerField()
    activity_type = models.CharField(max_length=20, choices=Activity.ActivityType.choices)

    class Meta:
        ordering = ['fitness_level', 'title']
