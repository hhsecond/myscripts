from typing import List, Set, Dict, Tuple, Text, Optional, AnyStr


def sum_and_stringify(nums: List[int]) -> str:  
    """Adds up the numbers in a list and returns the result as a string."""
    return str(sum(nums))


# For simple built-in types, just use the name of the type.
x = 1  # type: int
x = 1.0  # type: float
x = True  # type: bool
x = "test"  # type: str
x = u"test"  # type: str
x = b"test"  # type: bytes

# For collections, the name of the type is capitalized, and the
# name of the type inside the collection is in brackets.
x = [1]  # type: List[int]
x = {6, 7}  # type: Set[int]

# For mappings, we need the types of both keys and values.
x = {'field': 2.0}  # type: Dict[str, float]

# For tuples, we specify the types of all the elements.
x = (3, "yes", 7.5)  # type: Tuple[int, str, float]

# For textual data, use Text.
# This is `unicode` in Python 2 and `str` in Python 3.
x = ["string", u"unicode"]  # type: List[Text]



# Use Optional for values that could be None.
input_str = f()  # type: Optional[str]
if input_str is not None:
   print(input_str)