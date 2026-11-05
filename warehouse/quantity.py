"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Return the integer quantity parsed from *value*.

    Raises:
        ValueError: if *value* does not represent a valid positive integer
                    or if the parsed quantity is negative.
    """
    result = int(value.strip())
    if result < 0:
        raise ValueError(f"Quantity must be non-negative, got {result}")
    return result
