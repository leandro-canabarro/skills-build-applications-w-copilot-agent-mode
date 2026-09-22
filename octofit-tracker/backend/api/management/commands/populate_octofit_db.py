from datetime import datetime, timezone

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from api.models import Activity, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion


class Command(BaseCommand):
    help = 'Create the sample OctoFit Tracker data.'

    def handle(self, *args, **options):
        users = {}
        user_data = [
            ('alex', 'Alex Morgan', 'intermediate'),
            ('jordan', 'Jordan Lee', 'beginner'),
            ('sam', 'Sam Rivera', 'advanced'),
        ]
        for username, display_name, fitness_level in user_data:
            user, created = User.objects.get_or_create(
                username=username,
                defaults={'first_name': display_name.split()[0], 'last_name': display_name.split()[-1]},
            )
            if created:
                user.set_password('octofit-demo')
                user.save(update_fields=['password'])
            UserProfile.objects.update_or_create(
                user=user,
                defaults={'display_name': display_name, 'fitness_level': fitness_level},
            )
            users[username] = user

        team_data = {
            'Trail Blazers': ('Run together, grow together.', ['alex', 'sam']),
            'Daily Movers': ('Small steps count every day.', ['jordan']),
        }
        for name, (description, members) in team_data.items():
            team, _ = Team.objects.update_or_create(name=name, defaults={'description': description})
            team.members.set([users[username] for username in members])

        activity_data = [
            ('alex', Activity.ActivityType.RUN, 35, '5.20', 52, datetime(2026, 9, 18, 7, 30, tzinfo=timezone.utc)),
            ('jordan', Activity.ActivityType.WALK, 25, '2.10', 25, datetime(2026, 9, 19, 16, 0, tzinfo=timezone.utc)),
            ('sam', Activity.ActivityType.STRENGTH, 45, None, 60, datetime(2026, 9, 20, 18, 15, tzinfo=timezone.utc)),
        ]
        for username, activity_type, duration, distance, points, completed_at in activity_data:
            Activity.objects.update_or_create(
                user=users[username],
                activity_type=activity_type,
                completed_at=completed_at,
                defaults={
                    'duration_minutes': duration,
                    'distance_km': distance,
                    'points': points,
                },
            )

        leaderboard_points = {'sam': 120, 'alex': 104, 'jordan': 75}
        for rank, (username, points) in enumerate(leaderboard_points.items(), start=1):
            LeaderboardEntry.objects.update_or_create(
                user=users[username],
                defaults={'points': points, 'rank': rank},
            )

        suggestions = [
            ('Easy 20-minute walk', 'A relaxed walk to build a consistent movement habit.', 'beginner', 20, Activity.ActivityType.WALK),
            ('Steady 5K run', 'A comfortable run with a short warm-up and cool-down.', 'intermediate', 35, Activity.ActivityType.RUN),
            ('Full-body strength circuit', 'Four rounds of controlled bodyweight strength exercises.', 'advanced', 45, Activity.ActivityType.STRENGTH),
        ]
        for title, description, fitness_level, duration, activity_type in suggestions:
            WorkoutSuggestion.objects.update_or_create(
                title=title,
                defaults={
                    'description': description,
                    'fitness_level': fitness_level,
                    'duration_minutes': duration,
                    'activity_type': activity_type,
                },
            )

        self.stdout.write(self.style.SUCCESS('OctoFit Tracker database populated successfully.'))
