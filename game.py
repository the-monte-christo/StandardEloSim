import random
from player import Player

class Game:
    def __init__(self, player_a: Player, player_b: Player, k_factor: float = 32):
        """
        Initialisiert ein Spiel zwischen zwei Spielern.
        player_a, player_b: Spieler-Objekte
        k_factor: K-Faktor für das Elo-Update
        """
        self.player_a = player_a
        self.player_b = player_b
        self.k = k_factor

    def play(self) -> tuple[float, float]:
        """
        Führt ein Spiel aus:
        - Outcome wird gemäß "talent" entschieden (True Skill).
        - Elo-Werte werden anschließend aktualisiert.

        Rückgabe:
        (score_a, score_b)
        """
        # Sieg-Wahrscheinlichkeit basierend auf Talent
        prob_a = 1 / (1 + 10 ** ((self.player_b.talent - self.player_a.talent) / 400))
        # Ausspielung des Ergebnisses
        score_a = 1.0 if random.random() < prob_a else 0.0
        score_b = 1.0 - score_a

        # Elo-Updates
        self.player_a.update_elo(self.player_b, score_a, self.k)
        self.player_b.update_elo(self.player_a, score_b, self.k)

        return score_a, score_b
