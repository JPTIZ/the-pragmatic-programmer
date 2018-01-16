'''Address book database management.'''
from struct import pack, iter_unpack
from typing import NamedTuple


class Address(NamedTuple):
    name: str
    phone: str
    address: str
    number: int


def save(data, filename='book.db'):
    with open(filename, 'wb') as f:
        for item in data:
            _data = [elm.encode('utf-8') if isinstance(elm, str) else elm
                     for elm in item]
            f.write(pack('30s30s30si', *_data))


def load(data, filename='book.db'):
    def to_str(text):
        return text.decode('utf-8').split('\0')[0]

    with open(filename, 'rb') as f:
        return [Address(
                 name=to_str(name),
                 phone=to_str(phone),
                 address=to_str(address),
                 number=int(number))
                for name, phone, address, number in iter_unpack('30s30s30si',
                                                                f.read())]


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
