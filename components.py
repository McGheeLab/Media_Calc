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
        'cost': 44.25,                      # Cost in USD
        'catalog_number': 'ICN1676045',    # Catalog number
    },
    {
        'name': 'Streptomycin',
        'initial_weight': 10000,         # Amount
        'initial_weight_unit': 'ug',     # Unit
        'molecular_weight': 1457.4,      # g/mol
        'desired_stock_concentration': 10000,  # Concentration
        'stock_unit': 'ug/mL',           # Unit
        'solvent': 'Water',
        'cost': 29.56,                      # Cost in USD
        'catalog_number': '15140122',      # Catalog number
    },
    {
        'name': 'Noggin',
        'initial_weight': 50,            # Amount
        'initial_weight_unit': 'ug',     # Unit
        'molecular_weight': 64e3,        # g/mol (64 kDa)
        'desired_stock_concentration': 100,  # Concentration
        'stock_unit': 'ug/mL',           # Unit
        'solvent': 'PBS with 0.1% BSA',
        'cost': 202.13,                      # Cost in USD
        'catalog_number': '103872-972',      # Catalog number
    },
    {
        'name': 'Ascorbate-2-phosphate',
        'initial_weight': 5,             # Amount
        'initial_weight_unit': 'g',      # Unit
        'molecular_weight': 258.1,       # g/mol
        'desired_stock_concentration': 200,   # Concentration
        'stock_unit': 'mM',              # Unit
        'solvent': 'Water',
        'cost': 94.70,                      # Cost in USD
        'catalog_number': 'A8960-5g',       # Catalog number
    },
    {
        'name': 'Nicotinamide',
        'initial_weight': 500,           # Amount
        'initial_weight_unit': 'g',      # Unit
        'molecular_weight': 122.12,      # g/mol
        'desired_stock_concentration': 1,     # Concentration
        'stock_unit': 'M',               # Unit
        'solvent': 'Water',
        'cost': 116.58,                      # Cost in USD
        'catalog_number': 'N0636-500G',     # Catalog number
    },
    {
        'name': 'SB202190',
        'initial_weight': 5,             # Amount
        'initial_weight_unit': 'mg',     # Unit
        'molecular_weight': 377.4,       # g/mol
        'desired_stock_concentration': 10,    # Concentration
        'stock_unit': 'mM',              # Unit
        'solvent': 'DMSO',
        'cost': 138,                      # Cost in USD
        'catalog_number': 'S7067-5MG',     # Catalog number
    },
    {
        'name': 'A83-01',
        'initial_weight': 5,             # Amount
        'initial_weight_unit': 'mg',     # Unit
        'molecular_weight': 312.3,       # g/mol
        'desired_stock_concentration': 10,    # Concentration
        'stock_unit': 'mM',              # Unit
        'solvent': 'DMSO',
        'cost': 96.10,                      # Cost in USD
        'catalog_number': 'SML0788-5MG',   # Catalog number
    },
    {
        'name': 'AlbuMAX',
        'initial_weight': 25,            # Amount
        'initial_weight_unit': 'g',      # Unit
        'molecular_weight': None,        # Not applicable
        'desired_stock_concentration': 100,   # Concentration
        'stock_unit': 'mg/mL',           # Unit
        'solvent': 'Water',
        'cost': 138,                      # Cost in USD
        'catalog_number': '11020021',     # Catalog number
    },
    {
        'name': 'KGF',
        'initial_weight': 10,            # Amount
        'initial_weight_unit': 'ug',     # Unit
        'molecular_weight': 19.2e3,      # g/mol (19.2 kDa)
        'desired_stock_concentration': 100,   # Concentration
        'stock_unit': 'ug/mL',           # Unit
        'solvent': '0.1% BSA in PBS',
        'cost': 195,                      # Cost in USD
        'catalog_number': 'CYT-219',       # Catalog number
    },
    {
        'name': 'R-spondin I',
        'initial_weight': 100,           # Amount
        'initial_weight_unit': 'ug',     # Unit
        'molecular_weight': 27.9e3,      # g/mol (27.9 kDa)
        'desired_stock_concentration': 100,   # Concentration
        'stock_unit': 'ug/mL',           # Unit
        'solvent': 'PBS',
        'cost': 953,                      # Cost in USD
        'catalog_number': '4645-RS-100/CF',       # Catalog number
    },
    {
        'name': 'EGF',
        'initial_weight': 200,           # Amount
        'initial_weight_unit': 'ug',     # Unit
        'molecular_weight': 6.2e3,       # g/mol (6.2 kDa)
        'desired_stock_concentration': 100,   # Concentration
        'stock_unit': 'ug/mL',           # Unit
        'solvent': 'PBS',
        'cost': 147,                      # Cost in USD
        'catalog_number': '236-EG-200',       # Catalog number
    },
    {
        'name': '[Leu15]-Gastrin I',
        'initial_weight': 1,             # Amount
        'initial_weight_unit': 'mg',     # Unit
        'molecular_weight': 2094.4,      # g/mol
        'desired_stock_concentration': 1,     # Concentration
        'stock_unit': 'mM',              # Unit
        'solvent': 'Water',
        'cost': 424,                      # Cost in USD
        'catalog_number': '3006/1',     # Catalog number
    },
    {
        'name': 'Insulin',
        'initial_weight': 100,           # Amount
        'initial_weight_unit': 'mg',     # Unit
        'molecular_weight': 5808,        # g/mol
        'desired_stock_concentration': 10,    # Concentration
        'stock_unit': 'mg/mL',           # Unit
        'solvent': '0.01 N HCl',
        'cost': 231,                      # Cost in USD
        'catalog_number': '11376497001',     # Catalog number
    },
    {
        'name': 'Glucagon',
        'initial_weight': 5,             # Amount
        'initial_weight_unit': 'mg',     # Unit
        'molecular_weight': 3483.7,      # g/mol
        'desired_stock_concentration': 1,     # Concentration
        'stock_unit': 'mM',              # Unit
        'solvent': 'Water',
        'cost': 292.36,                      # Cost in USD
        'catalog_number': 'G2044-5MG',     # Catalog number
    },
    {
        'name': 'Wnt3a',
        'initial_weight': 100,           # Amount
        'initial_weight_unit': 'ug',     # Unit
        'molecular_weight': 39.9e3,      # g/mol (39.9 kDa)
        'desired_stock_concentration': 100,   # Concentration
        'stock_unit': 'ug/mL',           # Unit
        'solvent': 'PBS',
        'cost': 434,                      # Cost in USD
        'catalog_number': '5036-WN-010',     # Catalog number
    },
    # Existing components (antibiotics) with pre-made stock solutions
    {
        'name': 'Insulin/Transferrin/Selenium (ITS)',
        'stock_concentration': None,  # Dilution-based
        'stock_unit': None,
        'cost': 10,                      # Cost in USD
    },
    # Add additional components as needed
]
