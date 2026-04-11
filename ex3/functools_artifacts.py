from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable, Any

def spell_reducer(spells: list[int], operation: str) -> int:
    try:
        if len(spells) == 0:
            return 0
        my_operations = {"add": add, "multiply": mul, "max": max, "min": min}
        initializers = {"add": 0, "multiply": 1}
        if initializers.get(operation) is None:
            return reduce(my_operations[operation], spells)
        else:
            return reduce(my_operations[operation], spells, initializers.get(operation))
    except KeyError:
        raise KeyError("the operation is invalid")
    
def spell(power: int, element:str, target: str) -> str:
    return f"{element} engulfs {target} in flames, dealing {power} fire damage!"

def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "version1": partial(base_enchantment, power=50, element="Fireball"),
        "version2": partial(base_enchantment, power=50, element="Lightning"),
        "version3": partial(base_enchantment, power=50, element="Wind"),
            }



@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def spell(arg: Any):
        return "Unknown spell type"

    @spell.register(int)
    def _(damage_spell: int):
        return f"{damage_spell} damage"
    
    @spell.register(str)
    def _(enchantment: str):
        return enchantment
    
    @spell.register(list)
    def _(multiple_spells: list):
        return f"{len(multiple_spells)} spells"
    
    return spell

if __name__ == "__main__":
    try:
        print("\nTesting spell reducer...")
        print(f"Sum: {spell_reducer([20, 30, 50], "add")}")
        print(f"Product: {spell_reducer([20, 300, 400], "multiply")}")
        print(f"Max: {spell_reducer([33, 21, 16, 40], "max")}")

        print("\nTesting partial_enchanter...")
        func = partial_enchanter(spell)
        print(func['version1'](target='Dragon'))
        print(func['version3'](target='Wizard'))
        print(func['version3'](target='Dragon'))


        print("\nTesting memoized fibonacci...")
        print(f"Fib(0): {memoized_fibonacci(0)}")
        print(f"Fib(1): {memoized_fibonacci(1)}")
        print(f"Fib(10): {memoized_fibonacci(10)}")
        print(f"Fib(15): {memoized_fibonacci(15)}")

        # print(memoized_fibonacci.cache_info())

        print("\nTesting spell dispatcher...")
        spell = spell_dispatcher()
        print(f"Damage spell: {spell(42)}")
        print(f"Enchantment: {spell("fireball")}")
        print(f"Multi_cast: {spell([2, 4, 5])}")
        print(f"{spell((1, 2))}")

    except KeyError as e:
        print(e)