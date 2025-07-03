# player.py


class Player:
    def __init__(self, name: str, elo: float = 1200.0, talent: float = 1200.0):
        """
        name: Spielername
        elo: aktuelles Rating, das wir tracken
        talent: wahres Skill-Level (True Skill), skaliert wie Elo
        """
        self.name = name
        self.elo = elo
        self.initial_elo = elo  # Für Regression zur Mitte
        self.talent = talent

    def expected_score(self, opponent: 'Player') -> float:
        """Erwartete Sieg-Wahrscheinlichkeit basierend auf aktuellem Elo."""
        return 1 / (1 + 10 ** ((opponent.elo - self.elo) / 400))

    def update_elo(self, opponent: 'Player', score: float, k: float):
        """
        Aktualisiert das Elo basierend auf dem tatsächlichen Ergebnis,
        inklusive Regression-to-the-mean und minimalem Gain für Elo=0.
        score: 1.0=Sieg, 0.5=Unentschieden, 0.0=Niederlage
        k: K-Faktor
        """
        exp = self.expected_score(opponent)
        delta = k * (score - exp)
        new_elo = self.elo + delta
        # Regression to the mean: leichter Zug zurück zum Start-Elo
        lambda_reg = 0.001
        new_elo -= lambda_reg * (new_elo - self.initial_elo)
        # Minimaler Gain für Spieler auf 0 bei Sieg
        if self.elo <= 0 and score > 0:
            min_gain = 1.0
            new_elo = max(new_elo, min_gain)
        # Elo darf nicht negativ werden
        self.elo = max(0.0, new_elo)