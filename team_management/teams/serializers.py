from rest_framework import serializers
from .models import Team, Person


class TeamSerializer(serializers.ModelSerializer):
    """
    Serializer for Team objects.
    """
    class Meta:
        model = Team
        fields = ['id', 'name']


class PersonSerializer(serializers.ModelSerializer):
    """
    Serializer for Person objects.
    """
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'email', 'team']
