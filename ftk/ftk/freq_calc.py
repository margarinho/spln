# As frequencias relativas são dicionarios 
def racio(relative_P, relative_in):
    result = {}
    zero = 1 / sum(relative_P.values())
    
    for (word, value) in relative_in:
        result[word] = value/relative_P.get(word, zero)
    
    return dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
