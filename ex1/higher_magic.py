from typing import Callable

def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"

def fireball(target: str, power: int) -> str:
    return f"Fireball engulfs {target} in flames, dealing {power} fire damage!"

def blizzard(target: str, power: int) -> str:
    return f"Blizzard freezes {target} in a storm of ice, dealing {power} frost damage!"

def meteor(target: str, power: int) -> str:
    return f"Meteor crashes down on {target} from the sky, dealing {power} cosmic damage!"


def power_is_small(target: str, power: int) -> bool:
    return len(target)> 5 and power < 5



def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combine_spells(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combine_spells


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def multiply_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return multiply_spell

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def new_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return new_spell

def spell_sequence(spells: list[Callable]) -> Callable:
    def all_spells(target: str, power: int) -> list:
        my_spells = [spell(target, power) for spell in spells]
        return my_spells
    return all_spells

if __name__ == "__main__":
    combined = spell_combiner(fireball, heal)
    # print(fireball("Dragon", 3))
    # print(heal("Dragon", 3))
    print(combined("Dragon", 3))

    multiplied = power_amplifier(meteor, 2)
    print(multiplied("Wizard", 4))

    new_spell = conditional_caster(power_is_small, blizzard)
    print(new_spell("Knight", 2))

    my_spells = spell_sequence([fireball, heal, meteor])
    print(my_spells("Goblin", 5))
