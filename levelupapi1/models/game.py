from tkinter import CASCADE
from django.db import models

from levelupapi1.models import game_type


class Game(models.Model):

    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()