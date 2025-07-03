import random
from population import Population
from simulation import Simulation


talent_dist = lambda: random.uniform(300, 2000)
pop = Population.create_random(1000, 1000.0, talent_dist)
sim = Simulation(pop,
                k_factor=32,
                generations=600,
                elo_tolerance=150.0,
                random_match_chance=0.1,
                leave_count=2,
                join_count=3,
                join_max_elo=2000,
                join_min_elo= 1700)
history = sim.run()
print("Sim ready. Now Export!")
sim.export_frames('C:/temp/EloProject/frames', fixed_xlim=(0, 2500), fixed_ylim=(0,250), bins=30, mode='histogram')
sim.make_video('C:/temp/EloProject/simulation.mp4', fps=60)