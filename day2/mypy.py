def calc_total(lst: list[int]) -> int:
    return sum(lst)


calc_total([1, 2, 3])
calc_total([2, 3, "4"])

# mypy mypy.py
# pyright (or) pyright mypy.py
