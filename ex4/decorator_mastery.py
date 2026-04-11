from typing import Callable
from time import time
from functools import wraps
from random import random

def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"Spell completed in {end - start:.3f} seconds")
        return result
    return wrapper

@spell_timer
def add(a, b, c):
    return a + b + c


def power_validator(min_power: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = args[0] if args else kwargs.get('power')
            if power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator

@power_validator(3)
def fireball(power: int):
    return "good job"


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for x in range(1,max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt{x}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


@retry_spell(3)
def unstable_spell():
    if random() < 0.7:
        raise Exception("Spell fizzled!")
    return "Spell succeeded!"

class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(
            c.isalpha() or c.isspace() for c in name
        )
    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"

if __name__ == "__main__":
    add(20, 40, 50)
    print(fireball(power=1))
    print(unstable_spell())

    print("Testing MageGuild...")
    mage_1 = MageGuild
    mage_2 = MageGuild
    print(mage_1.validate_mage_name("Alex"))
    print(mage_2.validate_mage_name("Ash_ly"))
    print(mage_1.cast_spell(self=mage_1, spell_name="Alex", power=15))
    print(mage_2.cast_spell(self=mage_2, spell_name="Ash_ly", power=7))