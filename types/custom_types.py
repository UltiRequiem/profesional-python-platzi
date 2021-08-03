from typing import Tuple, Dict, List

CoordinatesType = List[Dict[str, Tuple[int, int]]]

coordinates: CoordinatesType = [
    {"coord_one": (1, 2), "coord_two": (3, 5)},
    {"coord_one": (0, 1), "coord_two": (2, 5)},
]

# https://stackoverflow.com/questions/68615894
