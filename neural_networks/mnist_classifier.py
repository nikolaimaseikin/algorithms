def avg(ranks):    
    assert len(ranks) != 0    
    return round(sum(ranks)/len(ranks), 2)
ranks = []
print("Среднее значение:", avg(ranks))