from rest_framework import viewsets
from .models import Team, Person
from .serializers import TeamSerializer, PersonSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Team objects.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing Person objects.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
