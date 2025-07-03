from typing import Callable, List, Tuple
from player import Player

class Population:
    def __init__(self, players: List[Player]):
        """
        Repräsentiert eine Gruppe von Spielern.
        players: Liste von Player-Instanzen
        """
        self.players = players

    @classmethod
    def create_random(cls, num_players: int, init_elo: float, talent_dist: Callable[[], float]) -> 'Population':
        """
        Erzeugt eine Population mit num_players Spielern,
        alle starten mit init_elo, erhalten aber unterschiedliche Talente.
        talent_dist: Funktion, die ein True Skill-Level zurückgibt.
        """
        players = [
            Player(name=f"P{i+1}", elo=init_elo, talent=talent_dist())
            for i in range(num_players)
        ]
        return cls(players)

# Beispiel für das Erstellen einer Population mit 1000 Spielern:
# import random
# talent_distribution = lambda: random.uniform(1000, 1400)
# pop = Population.create_random(num_players=1000, init_elo=1200.0, talent_dist=talent_distribution)
# print(f"Anzahl Spieler: {len(pop.players)} | Erster Talent-Wert: {pop.players[0].talent}")