from django.contrib import admin

from .models import Activity, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_name', 'fitness_level')
    search_fields = ('display_name', 'user__username')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    filter_horizontal = ('members',)


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity_type', 'duration_minutes', 'points', 'completed_at')
    list_filter = ('activity_type', 'completed_at')


@admin.register(LeaderboardEntry)
class LeaderboardEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'points', 'rank')


@admin.register(WorkoutSuggestion)
class WorkoutSuggestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'fitness_level', 'duration_minutes', 'activity_type')
    list_filter = ('fitness_level', 'activity_type')
