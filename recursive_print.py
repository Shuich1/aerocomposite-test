from typing import Optional, Union, Callable


def recursive_print(value: Optional[Union[int, float]] = 0) -> Callable[..., Union['recursive_print', Union[int, float]]]:
    """
    Returns a function that adds up its argument(s) and returns the result.

    Args:
        value (Optional[Union[int, float]], optional): The initial value to start adding from.
            Defaults to 0.

    Returns:
        Callable[..., Union['recursive_print', Union[int, float]]]: A function that takes an
            optional argument to add to the running total and returns either itself or the total,
            depending on whether an argument is passed.
    """
    def inner(next_value: Optional[Union[int, float]]= 0):
        nonlocal value
        value += next_value

        return inner if next_value else value

    return inner


if __name__ == "__main__":
    assert recursive_print(5)() == 5
    assert recursive_print(5)(10)() == 15
    assert recursive_print(15)(30)(-10)() == 35
