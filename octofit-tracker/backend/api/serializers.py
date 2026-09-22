from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Activity, LeaderboardEntry, Team, UserProfile, WorkoutSuggestion


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['display_name', 'bio', 'fitness_level']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, allow_blank=False)
    display_name = serializers.CharField(required=False, allow_blank=True)
    bio = serializers.CharField(required=False, allow_blank=True)
    fitness_level = serializers.CharField(required=False, allow_blank=True, default='beginner')

    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 'password',
            'display_name', 'bio', 'fitness_level',
        ]
        extra_kwargs = {
            'email': {'required': True},
            'username': {'required': True},
        }

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError('Email is required.')

        user_pk = self.instance.pk if self.instance else None
        queryset = User.objects.filter(email__iexact=value)
        if user_pk is not None:
            queryset = queryset.exclude(pk=user_pk)

        if queryset.exists():
            raise serializers.ValidationError('A user with this email already exists.')
        return value

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        display_name = validated_data.pop('display_name', '')
        bio = validated_data.pop('bio', '')
        fitness_level = validated_data.pop('fitness_level', 'beginner')

        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()

        UserProfile.objects.update_or_create(
            user=user,
            defaults={
                'display_name': display_name or user.get_full_name() or user.username,
                'bio': bio,
                'fitness_level': fitness_level,
            },
        )
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        display_name = validated_data.pop('display_name', None)
        bio = validated_data.pop('bio', None)
        fitness_level = validated_data.pop('fitness_level', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()

        profile_defaults = {}
        if display_name is not None:
            profile_defaults['display_name'] = display_name
        if bio is not None:
            profile_defaults['bio'] = bio
        if fitness_level is not None:
            profile_defaults['fitness_level'] = fitness_level

        if profile_defaults:
            UserProfile.objects.update_or_create(user=instance, defaults=profile_defaults)

        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        profile = getattr(instance, 'profile', None)
        display_name = profile.display_name if profile else instance.get_full_name() or instance.username
        bio = profile.bio if profile else ''
        fitness_level = profile.fitness_level if profile else 'beginner'

        representation['display_name'] = display_name
        representation['bio'] = bio
        representation['fitness_level'] = fitness_level
        return representation


class TeamSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, required=False)

    class Meta:
        model = Team
        fields = ['id', 'name', 'description', 'members']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['members'] = [member.id for member in instance.members.all()]
        return data


class ActivitySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Activity
        fields = ['id', 'user', 'activity_type', 'duration_minutes', 'distance_km', 'points', 'completed_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user_details'] = {
            'id': instance.user.id,
            'username': instance.user.username,
            'display_name': getattr(instance.user.profile, 'display_name', instance.user.get_full_name() or instance.user.username),
        }
        return data


class LeaderboardEntrySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = LeaderboardEntry
        fields = ['id', 'user', 'points', 'rank']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user_details'] = {
            'id': instance.user.id,
            'username': instance.user.username,
            'display_name': getattr(instance.user.profile, 'display_name', instance.user.get_full_name() or instance.user.username),
        }
        return data


class WorkoutSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSuggestion
        fields = ['id', 'title', 'description', 'fitness_level', 'duration_minutes', 'activity_type']
