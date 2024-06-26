from django.db import models


class Team(models.Model):
    """
    Team model.
    Attributes:
        name (str):  The name of the team.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    """
    Person model.
    Attributes:
        first_name (str): First name of the person.
        last_name (str): Last name of the person.
        email (str): Email address of the person. Unique.
        team (Team): Foreign key to Team model, representing the team the person belongs to.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, related_name='members', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
