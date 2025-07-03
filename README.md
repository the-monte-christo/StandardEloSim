# Standard Elo Simulator

**Standard Elo Simulator** dient dazu, die Standard-Elo-Formel über mehrere Runden (Generationen) hinweg zu simulieren. Für jede Generation werden Bilder erzeugt, die anschließend zu einem Film zusammengerendert werden können.

## Funktionen

- **Elo-Simulation**: Simuliert das Elo-Bewertungssystem über beliebig viele Runden/Generationen.
- **Bild-Export**: Erstellt für jede Generation eine Visualisierung als Bild.
- **Film-Erstellung**: Die generierten Bilder können zu einem Film (z.B. GIF oder Video) zusammengestellt werden.

## Verwendung

1. **Simulation starten**  
   Starte die Simulation und lege fest, wie viele Generationen du simulieren möchtest.

2. **Bilder generieren**  
   Nach jeder Generation wird ein Bild exportiert, das den Zustand der Simulation visualisiert.

3. **Film rendern**  
   Die einzelnen Bilder können mit Tools wie `ffmpeg` zu einem Film zusammengestellt werden.

## Beispiel (Pseudocode)

```python
for generation in range(anzahl_generationen):
    simuliere_elo_runde()
    exportiere_generationsbild(generation)
render_film_aus_bildern()
```

## Lizenz

**Public Domain**  
Dieses Projekt ist gemeinfrei (public domain). Es darf beliebig genutzt, verändert und weitergegeben werden – ohne Einschränkungen.

```
CC0 1.0 Universal (CC0 1.0) Public Domain Dedication
```
