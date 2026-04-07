import random

def simulate_crashes(days):
    """
    Simulates server crashes for a given number of days.
    Returns: (total_crashes, simulated_probability)
    """
    crashes = 0
    for _ in range(days):
        if random.random() < 0.045:  # 4.5% chance of crash
            crashes += 1

    probability = crashes / days
    return crashes, probability