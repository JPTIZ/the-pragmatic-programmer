'''Address book database management.'''
import json

from typing import NamedTuple


class Address(NamedTuple):
    name: str
    phone: str
    address: str
    number: int


def save(data, filename='book.db'):
    with open(filename, 'w') as f:
        json.dump(data, fp=f)


def load(data, filename='book.db'):
    with open(filename, 'rb') as f:
        return [Address(*item) for item in json.load(f)]


if __name__ == '__main__':
    data = [
            Address(name='Alice',
                    phone='0000-0000',
                    address='Street',
                    number=0),
            Address(name='Bob',
                    phone='1111-1111',
                    address='Road',
                    number=1),
            Address(name='C',
                    phone='2222-2222',
                    address='Avenue',
                    number=42),
            Address(name='Eva',
                    phone='6666-6666',
                    address='Nowhere',
                    number=66),
            ]
    save(data)
    for item in load(data):
        print(item)
