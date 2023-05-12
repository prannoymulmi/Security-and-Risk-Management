from ahpy import ahpy

supply_chain_comp = {
    ('Digital Prepardness', 'Digital Prepardness'): 1, ('Digital Prepardness', 'Natural Disasters'): 6, ('Digital Prepardness', 'Labor Strikes'): 8, ('Digital Prepardness', 'Political Instability'): 4, ('Digital Prepardness', 'Logistic Index'): 3,
    ('Natural Disasters', 'Digital Prepardness'): 1/6, ('Natural Disasters', 'Natural Disasters'): 1, ('Natural Disasters', 'Labor Strikes'): 3, ('Natural Disasters', 'Political Instability'): 1/2, ('Natural Disasters', 'Logistic Index'): 1/5,
    ('Labor Strikes', 'Digital Prepardness'): 1/8, ('Labor Strikes', 'Natural Disasters'): 1/3, ('Labor Strikes', 'Labor Strikes'): 1, ('Labor Strikes', 'Political Instability'): 1/2, ('Labor Strikes', 'Logistic Index'): 1/4,
    ('Political Instability', 'Digital Prepardness'): 1/4, ('Political Instability', 'Natural Disasters'): 2, ('Political Instability', 'Labor Strikes'): 2, ('Political Instability', 'Political Instability'): 1, ('Political Instability', 'Logistic Index'): 1/3,
    ('Logistic Index', 'Digital Prepardness'): 1/3, ('Logistic Index', 'Natural Disasters'): 5, ('Logistic Index', 'Labor Strikes'): 4, ('Logistic Index', 'Political Instability'): 3, ('Logistic Index', 'Logistic Index'): 1
    }


supply_chain = ahpy.Compare(name='Supply_Chain', comparisons=supply_chain_comp, precision=5, random_index='saaty')

print(supply_chain.target_weights)
print(supply_chain.consistency_ratio)