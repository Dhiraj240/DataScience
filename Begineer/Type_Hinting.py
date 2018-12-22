# Provide a hint about data type consideration
# PEP8- Python Enhancement Proposal says leave 2 blank lines


def add_numbers(a: int, b: int) -> int:
    return a+b


print(add_numbers(10, 11))
# Display error on IDE to consider only integer data type
print(add_numbers(10, "string"))
