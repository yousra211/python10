from typing import Callable

def mage_counter() -> Callable:
    count = 0
    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power
    def total_counter(number: int) -> int:
        nonlocal total
        total += number
        return total
    return total_counter


def enchantment_factory(enchantment_type: str) -> Callable:
    def factory(name: str) -> str:
        

if __name__ == "__main__":
    # counter1 = mage_counter()
    # print(counter1())
    # print(counter1())
    # print(counter1())
    
    # counter2 = mage_counter()
    # print(counter2())
    # print(counter2())

    accumulator = spell_accumulator(2)
    print(accumulator(3))
    print(accumulator(3))