from population import Population
from player import Player
from typing import Optional,Callable, List, Tuple
from game import Game
import os
import matplotlib.pyplot as plt
from  moviepy import ImageSequenceClip
import shutil
import random


class SimulationGeneration:
    def __init__(self,
                 population: Population,
                 k_factor: float = 32,
                 elo_tolerance: float = 100.0,
                 random_match_chance: float = 0.1):
        self.population = population
        self.k = k_factor
        self.tolerance = elo_tolerance
        self.random_chance = random_match_chance

    def run_generation(self) -> List[Tuple[Player, Player, float, float]]:
        unmatched = self.population.players.copy()
        random.shuffle(unmatched)
        results = []
        while len(unmatched) > 1:
            a = unmatched.pop(0)
            if random.random() < self.random_chance:
                b = random.choice(unmatched)
                unmatched.remove(b)
            else:
                candidates = [p for p in unmatched if abs(p.elo - a.elo) <= self.tolerance]
                if candidates:
                    b = random.choice(candidates)
                    unmatched.remove(b)
                else:
                    b = unmatched.pop(0)
            result = Game(a, b, self.k).play()
            results.append((a, b, *result))
        return results

class Simulation:
    def __init__(self,
                 population: Population,
                 k_factor: float = 32,
                 generations: int = 10,
                 elo_tolerance: float = 100.0,
                 random_match_chance: float = 0.1,
                 leave_count: int = 0,
                 join_count: int = 0,
                 join_min_elo: int = 300,
                 join_max_elo: int = 2000):
        self.population = population
        self.k = k_factor
        self.generations = generations
        self.tolerance = elo_tolerance
        self.random_chance = random_match_chance
        self.leave_count = leave_count
        self.join_count = join_count
        self.join_max_elo = join_max_elo
        self.join_min_elo = join_min_elo
        self.history: List[dict[str, float]] = []
        self.frames_dir: Optional[str] = None
        self._next_id = len(self.population.players) + 1

    def run(self) -> List[dict[str, float]]:
        for _ in range(self.generations):
            SimulationGeneration(self.population, self.k,
                                 self.tolerance, self.random_chance).run_generation()
            snapshot = {p.name: p.elo for p in self.population.players}
            self.history.append(snapshot)
            # leave
            if self.leave_count and len(self.population.players) > self.leave_count:
                for p in random.sample(self.population.players, self.leave_count):
                    self.population.players.remove(p)
            # join
            for _ in range(self.join_count):
                base_elo = random.choice(list(snapshot.values()))
                new = Player(name=f"P{self._next_id}", elo=base_elo, talent=random.uniform(self.join_min_elo, self.join_max_elo))
                self.population.players.append(new)
                self._next_id += 1
        return self.history

    def export_frames(self,
                      output_dir: str,
                      fixed_xlim: Optional[Tuple[float, float]] = None,
                      fixed_ylim: Optional[Tuple[int, int]] = None,
                      bins: int = 20,
                      mode: str = 'histogram'):
        os.makedirs(output_dir, exist_ok=True)
        self.frames_dir = output_dir
        if fixed_xlim:
            min_elo, max_elo = fixed_xlim
        else:
            all_elos = [e for snap in self.history for e in snap.values()]
            min_elo, max_elo = min(all_elos), max(all_elos)
        for idx, snap in enumerate(self.history):
            elos = list(snap.values())
            plt.figure(figsize=(10, 6))
            if mode == 'histogram':
                plt.hist(elos, bins=bins, edgecolor='black')
                plt.ylabel('Anzahl Spieler')
            else:
                sorted_elos = sorted(elos)
                plt.scatter(sorted_elos, range(1, len(elos)+1), alpha=0.7)
                plt.ylabel('Rang')
            plt.xlim(min_elo, max_elo)
            if fixed_ylim:
                plt.ylim(fixed_ylim)
            plt.title(f"Generation {idx+1}")
            plt.xlabel('Elo')
            plt.tight_layout()
            plt.savefig(os.path.join(output_dir, f"frame_{idx:03d}.png"))
            plt.close()

    def make_video(self, output_path: str, fps: int = 10, cleanup: bool = True):
        if not self.frames_dir:
            raise RuntimeError("Please export frames first.")
        clip = ImageSequenceClip(self.frames_dir, fps=fps)
        clip.write_videofile(output_path, codec='libx264', audio=False)
        if cleanup:
            shutil.rmtree(self.frames_dir)
