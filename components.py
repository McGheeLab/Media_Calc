# components.py

components_stock = [
    {
        'name': 'Gentamicin',
        'initial_weight': 10,            # Amount
        'initial_weight_unit': 'mg',     # Unit
        'molecular_weight': 477.6,       # g/mol
        'desired_stock_concentration': 10,  # Concentration
        'stock_unit': 'mg/mL',           # Unit
        'solvent': 'Water',
    },
    {
        'name': 'Streptomycin',
        'initial_weight': 10000,         # Amount
        'initial_weight_unit': 'ug',     # Unit
        'molecular_weight': 1457.4,      # g/mol
        'desired_stock_concentration': 10000,  # Concentration
        'stock_unit': 'ug/mL',           # Unit
        'solvent': 'Water',
    },
    {
        'name': 'Noggin',
        'initial_weight': 50,            # Amount
        'initial_weight_unit': 'ug',     # Unit
        'molecular_weight': 64e3,        # g/mol (64 kDa)
        'desired_stock_concentration': 100,  # Concentration
        'stock_unit': 'ug/mL',           # Unit
        'solvent': 'PBS with 0.1% BSA',
    },
    {
        'name': 'Ascorbate-2-phosphate',
        'initial_weight': 5,             # Amount
        'initial_weight_unit': 'g',      # Unit
        'molecular_weight': 258.1,       # g/mol
        'desired_stock_concentration': 200,   # Concentration
        'stock_unit': 'mM',              # Unit
        'solvent': 'Water',
    },
    {
        'name': 'Nicotinamide',
        'initial_weight': 500,           # Amount
        'initial_weight_unit': 'g',      # Unit
        'molecular_weight': 122.12,      # g/mol
        'desired_stock_concentration': 1,     # Concentration
        'stock_unit': 'M',               # Unit
        'solvent': 'Water',
    },
    {
        'name': 'SB202190',
        'initial_weight': 5,             # Amount
        'initial_weight_unit': 'mg',     # Unit
        'molecular_weight': 377.4,       # g/mol
        'desired_stock_concentration': 10,    # Concentration
        'stock_unit': 'mM',              # Unit
        'solvent': 'DMSO',
    },
    {
        'name': 'A83-01',
        'initial_weight': 5,             # Amount
        'initial_weight_unit': 'mg',     # Unit
        'molecular_weight': 312.3,       # g/mol
        'desired_stock_concentration': 10,    # Concentration
        'stock_unit': 'mM',              # Unit
        'solvent': 'DMSO',
    },
    {
        'name': 'AlbuMAX',
        'initial_weight': 25,            # Amount
        'initial_weight_unit': 'g',      # Unit
        'molecular_weight': None,        # Not applicable
        'desired_stock_concentration': 100,   # Concentration
        'stock_unit': 'mg/mL',           # Unit
        'solvent': 'Water',
    },
    {
        'name': 'KGF',
        'initial_weight': 10,            # Amount
        'initial_weight_unit': 'ug',     # Unit
        'molecular_weight': 19.2e3,      # g/mol (19.2 kDa)
        'desired_stock_concentration': 100,   # Concentration
        'stock_unit': 'ug/mL',           # Unit
        'solvent': '0.1% BSA in PBS',
    },
    {
        'name': 'R-spondin I',
        'initial_weight': 100,           # Amount
        'initial_weight_unit': 'ug',     # Unit
        'molecular_weight': 27.9e3,      # g/mol (27.9 kDa)
        'desired_stock_concentration': 100,   # Concentration
        'stock_unit': 'ug/mL',           # Unit
        'solvent': 'PBS',
    },
    {
        'name': 'EGF',
        'initial_weight': 200,           # Amount
        'initial_weight_unit': 'ug',     # Unit
        'molecular_weight': 6.2e3,       # g/mol (6.2 kDa)
        'desired_stock_concentration': 100,   # Concentration
        'stock_unit': 'ug/mL',           # Unit
        'solvent': 'PBS',
    },
    {
        'name': '[Leu15]-Gastrin I',
        'initial_weight': 1,             # Amount
        'initial_weight_unit': 'mg',     # Unit
        'molecular_weight': 2094.4,      # g/mol
        'desired_stock_concentration': 1,     # Concentration
        'stock_unit': 'mM',              # Unit
        'solvent': 'Water',
    },
    {
        'name': 'Insulin',
        'initial_weight': 100,           # Amount
        'initial_weight_unit': 'mg',     # Unit
        'molecular_weight': 5808,        # g/mol
        'desired_stock_concentration': 10,    # Concentration
        'stock_unit': 'mg/mL',           # Unit
        'solvent': '0.01 N HCl',
    },
    {
        'name': 'Glucagon',
        'initial_weight': 5,             # Amount
        'initial_weight_unit': 'mg',     # Unit
        'molecular_weight': 3483.7,      # g/mol
        'desired_stock_concentration': 1,     # Concentration
        'stock_unit': 'mM',              # Unit
        'solvent': 'Water',
    },
    {
        'name': 'Wnt3a',
        'initial_weight': 100,           # Amount
        'initial_weight_unit': 'ug',     # Unit
        'molecular_weight': 39.9e3,      # g/mol (39.9 kDa)
        'desired_stock_concentration': 100,   # Concentration
        'stock_unit': 'ug/mL',           # Unit
        'solvent': 'PBS',
    },
    # Existing components (antibiotics) with pre-made stock solutions
    {
        'name': 'Insulin/Transferrin/Selenium (ITS)',
        'stock_concentration': None,  # Dilution-based
        'stock_unit': None,
    },
    # Add additional components as needed
]
