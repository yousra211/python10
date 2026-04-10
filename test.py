mages=[
    {"name": "fireball", "power": 85, "element": "fire"},
    {"name": "heal", "power": 80, "element": "healing"},
    {"name": "shield", "power": 94, "element": "shield"},
    ]

max_power = max(mages, key=lambda x: x['power'])['power']

print(max_power)
