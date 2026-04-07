import math

class StatEngine:
    def __init__(self, data):
        self.data = [x for x in data if isinstance(x, (int, float))]
        
        if len(self.data) == 0:
            raise ValueError("Data must contain at least one numeric value.")
    
    def get_mean(self):
        return sum(self.data) / len(self.data)
    
    def get_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        
        if n % 2 == 1:
            return sorted_data[mid]
        else:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    
    def get_mode(self):
        freq = {}
        for x in self.data:
            freq[x] = freq.get(x, 0) + 1
        
        max_count = max(freq.values())
        
        if max_count == 1:
            return "No mode (all values are unique)"
        
        return [k for k, v in freq.items() if v == max_count]
    
    def get_variance(self, is_sample=True):
        n = len(self.data)
        
        if is_sample and n < 2:
            raise ValueError("Sample variance requires at least 2 data points.")
        
        mean = self.get_mean()
        squared_diff = [(x - mean) ** 2 for x in self.data]
        
        if is_sample:
            return sum(squared_diff) / (n - 1)
        else:
            return sum(squared_diff) / n
    
    def get_standard_deviation(self, is_sample=True):
        return math.sqrt(self.get_variance(is_sample))
    
    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        std = self.get_standard_deviation()
        
        return [x for x in self.data if abs(x - mean) > threshold * std]