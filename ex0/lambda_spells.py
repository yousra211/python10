artifacts=[
    {"name": "Crystal Orb", "power": 85, "type": "spell"},
    {"name": "Fire Staff", "power": 92, "type": "spell"}
             ]

artifacts = sorted(artifacts, key=lambda x: x["power"], reverse=True)
print(f"{artifacts[0]['name']} ({artifacts[0]['power']} power) comes before {artifacts[1]['name']} ({artifacts[1]['power']}")

mages=[
    {"name": "fireball", "power": 85, "element": "fire"},
    {"name": "heal", "power": 80, "element": "healing"},
    {"name": "shield", "power": 94, "element": "shield"},
    ]

power_filter = lambda mages, min_power: list(filter(lambda x: x["power"] >= min_power, mages))
print(power_filter(mages, 85))