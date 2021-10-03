"""
ref: https://twitter.com/nikitonsky/status/1443959126338543616?s=08
"""
import numpy as np
from collections import defaultdict

input = [
    {"age": 18, "rate": 30},
    {"age": 18, "rate": 15},
    {"age": 50, "rate": 35}
]

def calculate_avg_rate(input: list) -> dict:
    result = dict()
    collected_dict = defaultdict(list)

    for i in input:
        collected_dict[i["age"]].append(i["rate"])
    
    for a in collected_dict:
        result[a] = np.array(collected_dict[a]).mean()
    
    return result

print(calculate_avg_rate(input))