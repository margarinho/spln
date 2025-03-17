# Calcus.py
# 12 de março de 2025

from collections import Counter 

def counter(tokens, num):
    counter = Counter(tokens)
    total_count = sum(counter.values())
    type(num)
    relative = {
        word: (int(count) / total_count) * num if isinstance(count, (int, float)) else 0
        for word, count in counter.most_common()
    }
    return counter, relative

def normalization (counter: list, total: int):
    for key in counter.keys():
        counter[key] = counter[key] / total
      
def surprise (counter_ref: dict, counter_cor: dict):
    ref_total = sum(counter_ref.values())
    cor_total = sum(counter_cor.values())
    zero = 1 / ref_total
    
    counter_ref = normalization(counter_ref, ref_total)
    counter_cor = normalization(counter_cor, cor_total)
    
    output = {}
    
    for key in counter_cor.keys():
        value_cor = counter_cor.get(key)
        value_ref = counter_ref.get(key, zero)
        output.append({key : value_cor / value_ref})
        
    return output