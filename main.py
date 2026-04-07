from src.stat_engine import StatEngine
from src.monte_carlo import simulate_crashes

data = [10, 12, 11, 100, 9, 10, 12]

# Creating StatEngine object
engine = StatEngine(data)


print("Mean:", engine.get_mean())
print("Median:", engine.get_median())
print("Mode:", engine.get_mode())

# Show outliers takind threshold = 2
print("Outliers:", engine.get_outliers())


print("\nServer crash simulation:")
for days in [30, 1000, 10000]:
    crashes, prob = simulate_crashes(days)
    print(f"{days} days → {crashes} crashes, simulated probability: {prob:.4f}")