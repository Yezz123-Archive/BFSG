from __future__ import annotations
import string
from enum import IntEnum


class Direction(IntEnum):
    LEFT = 0
    RIGHT = -1


class BruteForceStringGenerator:

    def __init__(self, sequence: str = '', chars: str = string.ascii_lowercase, direction: Direction = Direction.RIGHT,
                 min_length: int = 1, max_length: int = 0) -> None:

        self.sequence = sequence
        self._sequence_list = list(sequence)
        self.chars = chars
        self.dir = direction
        self.min_length = max(0, min_length)
        self.max_length = max(0, max_length)
        self.chars_num = len(self.chars)

    def __iter__(self) -> BruteForceStringGenerator:
        return self

    def __next__(self) -> str:
        self.next_string()
        return self.sequence

    def __len__(self) -> int:
        return len(self._sequence_list)

    def __repr__(self):
        return f"{self.sequence}"

    @property
    def sequence(self) -> str:
        return "".join(self._sequence_list)

    @sequence.setter
    def sequence(self, sequence: str) -> None:
        self._sequence_list = list(sequence)

    @property
    def dir(self):
        return self._dir

    @dir.setter
    def dir(self, direction):
        if type(direction) is not Direction:
            raise ValueError("Direction should be Direction Type")
        self._dir = direction

    @property
    def min_length(self):
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        if type(min_length) is not int or min_length <= 0:
            raise ValueError("min_length should be integer greater than 0")
        self._min_length = min_length

    @property
    def max_length(self):
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        if type(max_length) is not int or max_length < 0:
            raise ValueError("max_length should be integer")
        self._max_length = max_length

    def next_string(self) -> None:
        self._sequence_list = self._next(self._sequence_list)

    def check_length(self, length: int):
        if self.max_length and length > self.max_length:
            raise StopIteration

    def _next(self, current: list) -> list:
        if len(current) <= 0:
            if not self._sequence_list:
                return list(self.chars[0] * self.min_length)
            else:
                self.check_length(len(self) + 1)
                return list(self.chars[0])
        else:
            self.check_length(len(self))
            current[self.dir] = self.chars[((self.chars.index(current[self.dir]) + 1) % self.chars_num)]
            if self.chars.index(current[self.dir]) == 0:
                if self.dir == Direction.LEFT:
                    return list(current[0]) + self._next(current[1:])
                else:
                    return self._next(current[:-1]) + list(current[-1])
        return current
