"""
Strobogrammatic Number check function
@:param number: str - The number to check
@:return bool - True if the number is strobogrammatic, False otherwise
"""


def check(number: str) -> bool:
    map: dict[str, str] = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

    i: int = 0
    max: int = len(number) - 1

    while i <= max:
        if number[i] not in map or map[number[i]] != number[max]:
            return False
        i += 1
        max -= 1
    return True


"""
StrobogrammaticNumber class
"""


class StrobogrammaticNumber:
    pass
