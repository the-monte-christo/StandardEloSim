# Standard Elo Simulator

**Standard Elo Simulator** dient dazu, die Standard-Elo-Formel über mehrere Runden (Generationen) hinweg zu simulieren. Für jede Generation werden Bilder erzeugt, die anschließend zu einem Film zusammengerendert werden können.

## Funktionen

- **Elo-Simulation**: Simuliert das Elo-Bewertungssystem über beliebig viele Runden/Generationen.
- **Bild-Export**: Erstellt für jede Generation eine Visualisierung als Bild.
- **Film-Erstellung**: Die generierten Bilder können zu einem Film (z.B. GIF oder Video) zusammengestellt werden.

**StandardEloSim** ist ein einfach konzipierter, aber flexibel erweiterbarer **Elo-Rating-Simulator**. Ziel ist es, eine Population von Spielern mit fiktiven „Skill“-Werten (z. B. Naturtalente, Durchschnittsspieler) über viele Generationen hinweg in simulierten Spielen gegeneinander antreten zu lassen – und dabei zu beobachten, wie sich ihre Elo-Werte im Zeitverlauf entwickeln, stabilisieren oder verschieben.

Das Projekt eignet sich zur **Visualisierung von Rating-Dynamiken**, **Experimenten mit Matchmaking-Logik**, oder einfach zur spielerischen Modellierung von kompetitiven Systemen.

---

## 🧠 Motivation

- Wie genau ordnet ein Elo-System neue Spieler ein?
- Wie lange dauert es, bis sich die Ratings stabilisieren?
- Was passiert, wenn ein Spieler mit echtem „Top-Skill“ plötzlich ins System kommt?
- Wie verhalten sich schwache Spieler über viele Spiele hinweg?

Diese Fragen lassen sich mit **StandardEloSim** interaktiv untersuchen.

---

## 🚀 Features

- 🎲 Simulation von Matches auf Basis von Skill vs. Elo
- 📈 Automatische Anpassung der Elo-Werte nach jedem Spiel
- 👥 Spieler mit konstantem „wahren Skill“ und individuellem Start-Elo
- 🔄 Unterstützung für Simulationen über beliebig viele Runden / Generationen
- 📊 Vorbereitung für Visualisierung mit `matplotlib` (z. B. Ratings über Zeit)

---

## 📦 Struktur

- `elo.py` – Enthält die zentrale Elo-Berechnungslogik
- `player.py` – Definiert Spielerobjekte mit „Skill“ und „Elo“
- `simulation.py` – Führt Runden durch, wertet Spiele aus, passt Elo an
- `visualization.py` *(optional)* – Plotfunktionen zur Darstellung der Entwicklung
- `main.py` – Einstiegspunkt für komplette Simulation

---

## 🛠️ Nutzung

```bash
git clone https://github.com/the-monte-christo/StandardEloSim.git
cd StandardEloSim
python3 main.py


## Lizenz

**Public Domain**  
Dieses Projekt ist gemeinfrei (public domain). Es darf beliebig genutzt, verändert und weitergegeben werden – ohne Einschränkungen.

```
CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
```
