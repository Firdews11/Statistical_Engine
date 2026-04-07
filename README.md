# Statistical Engineering & Simulation

## Project Overview
This project implements a **pure Python statistical engine** (`StatEngine`) to analyze 1D numerical datasets. It calculates key statistical metrics including **mean, median, mode, variance, standard deviation, and outlier detection**. Additionally, it includes a **Monte Carlo simulation** to demonstrate the **Law of Large Numbers** using a startup server crash scenario.

---

## Mathematical Logic

- **Mean**: Sum of all values divided by the number of values.
- **Median**: Middle value after sorting the data. If the dataset has an even number of values, it returns the average of the two middle values.
- **Mode**: Most frequent value(s). If all values are unique, it returns a specific message.
- **Variance**: Measures data dispersion.  
  - **Population variance**: `sum((x - mean)^2) / n`  
  - **Sample variance (Bessel's correction)**: `sum((x - mean)^2) / (n-1)`
- **Standard Deviation**: Square root of the variance.
- **Outliers**: Data points further than a specified number of standard deviations from the mean (default threshold = 2).

---

## Setup Instructions

1. **Clone the repository:**
```bash
git clone <your-github-repo-link>