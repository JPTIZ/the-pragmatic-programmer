'''Address book database management.'''
from struct import pack, calcsize, unpack
from typing import NamedTuple


class Address(NamedTuple):
    name: str
    phone: str
    address: str
    number: int
    directions: str


def save(data, filename='book.db'):
    def to_str(text):
        return text.encode('utf-8')

    with open(filename, 'wb') as f:
        for item in data:
            _data = [
                     to_str(item.name),
                     to_str(item.phone),
                     to_str(item.address),
                     item.number,
                     len(item.directions),
                     to_str(item.directions),
                     ]
            dir_size = len(item.directions)
            f.write(pack(f'30s30s30sii{dir_size}s', *_data))


def load(data, filename='book.db'):
    def to_str(text):
        if isinstance(text, str):
            return text
        return text.decode('utf-8').split('\0')[0]

    def extract_addr(f):
        HEADER_FMT = "30s30s30sii"
        HEADER_SIZE = calcsize(HEADER_FMT)

        while True:
            file_bytes = f.read(HEADER_SIZE)
            if not file_bytes:
                return
            name, phone, address, number, n = unpack(HEADER_FMT,
                                                     file_bytes)
            directions_bytes = f.read(n)
            directions = directions_bytes.decode('utf-8')
            yield (to_str(name),
                   to_str(phone),
                   to_str(address),
                   number,
                   to_str(directions))

    with open(filename, 'rb') as f:
        return [Address(
                 name=to_str(name),
                 phone=to_str(phone),
                 address=to_str(address),
                 number=int(number),
                 directions=to_str(directions))
                for name, phone, address, number, directions
                in extract_addr(f)]


if __name__ == '__main__':
    data = [
            Address(name='Alice',
                    phone='0000-0000',
                    address='Street',
                    number=0,
                    directions='Walk forward for 3 turns.'),
            Address(name='Bob',
                    phone='1111-1111',
                    address='Road',
                    number=1,
                    directions='Go here then there and yay.'),
            Address(name='C',
                    phone='2222-2222',
                    address='Avenue',
                    number=42,
                    directions='Search for an avenue.'),
            Address(name='Eva',
                    phone='6666-6666',
                    address='Nowhere',
                    number=66,
                    directions='Good luck'),
            ]
    save(data)
    for item in load(data):
        print(item)
