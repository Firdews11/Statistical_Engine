from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes

# Example dataset for testing StatEngine
data = [10, 12, 11, 100, 9, 10, 12]

# Create StatEngine object
engine = StatEngine(data)

# Show central tendency
print("Mean:", engine.get_mean())
print("Median:", engine.get_median())
print("Mode:", engine.get_mode())

# Show outliers (default threshold = 2 standard deviations)
print("Outliers:", engine.get_outliers())

# Monte Carlo simulation
print("\nServer crash simulation:")
for days in [30, 1000, 10000]:
    crashes, prob = simulate_crashes(days)
    print(f"{days} days → {crashes} crashes, simulated probability: {prob:.4f}")