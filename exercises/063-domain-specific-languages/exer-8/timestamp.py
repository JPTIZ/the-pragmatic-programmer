'''Timestamp parsing module.'''
import re

from typing import NamedTuple


class Time(NamedTuple):
    hours: int
    minutes: int


def parse(text: str):
    h, m = re.compile(r'(\d{1,2})(?::(\d{2})|am|pm)').match(text).groups()
    return Time(hours=h, minutes=m or 0)


if __name__ == '__main__':
    print(parse('4pm'))
    print(parse('7:30pm'))
    print(parse('23:42'))
    print(parse('3:16'))
    print(parse('3:16am'))
