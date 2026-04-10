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
        return enchantment_type + " " + name
    return factory


def memory_vault() -> dict[str, Callable]:
    my_dict = {}
    def store(key: str, value: str) -> None:
        my_dict[key] = value

    def recall(key: str) -> str:
        return my_dict.get(key, "Memory not found")
    return {"store": store, "recall": recall}

if __name__ == "__main__":
    # counter1 = mage_counter()
    # print(counter1())
    # print(counter1())
    # print(counter1())
    
    # counter2 = mage_counter()
    # print(counter2())
    # print(counter2())

    # accumulator = spell_accumulator(2)
    # print(accumulator(3))
    # print(accumulator(3))

    vault = memory_vault()
    vault["store"]("shield", "6")
    print(vault["recall"]("shxield"))