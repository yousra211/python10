def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))

def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: '*' + x + '*', spells))

def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda x: x['power'])['power']
    min_power = min(mages, key=lambda x: x['power'])['power']
    avg_power = sum(x["power"] for x in mages) / len(mages)
    return {'max_power': max_power, 'min_power': min_power, 'avg_power': round(avg_power, 2)}


artifacts=[
    {"name": "Crystal Orb", "power": 85, "type": "weapon"},
    {"name": "Fire Staff", "power": 92, "type": "armor"}
             ]
print(f"{artifacts[0]['name']} ({artifacts[0]['power']} power) comes before {artifacts[1]['name']} ({artifacts[1]['power']})")
mages=[
    {"name": "fireball", "power": 85, "element": "fire"},
    {"name": "heal", "power": 80, "element": "healing"},
    {"name": "shield", "power": 94, "element": "wind"},
    ]
print(power_filter(mages, 85))

listt = spell_transformer(['fireball', 'heal', 'shield'])
for el in listt:
    print(el, end=' ')

stats = mage_stats(mages)
print(f"\n{stats}")
