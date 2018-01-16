'''Deals with language tools for data conversion, code generation and such.'''
import re

from typing import List, NamedTuple


class Comment(NamedTuple):
    text: str = ''


class Array(NamedTuple):
    inner_type: str
    length: int = -1


class Field(NamedTuple):
    name: str
    value_type: str
    comment: Comment = Comment('')


class DataType(NamedTuple):
    name: str
    fields: List[Field]


class Parser:
    def __init__(self):
        self.comment = Comment()
        self.types = []


def parse(text: str):
    def next_line(lines):
        return next(lines).split('#', maxsplit=1)

    def begin_type(lines, name, suffix=''):
        return DataType(name=f'{name}{suffix}', fields=parse_fields(lines))

    def parse_fields(lines):
        def extract_type(text):
            def as_array(field_type):
                match = re.compile('([a-zA-Z0-9]+)\[(\d*)\]').match(
                                   field_type)
                if match:
                    return Array(*match.groups())
                return None

            return (as_array(text) or
                    text)

        fields = []
        while True:
            line = next_line(lines)[0].split()
            command = line[0]
            if command == 'E':
                return fields
            elif command == 'F':
                field_name, field_type = line[1:]
                fields.append(Field(name=field_name,
                                    value_type=extract_type(field_type)))

    def common_parse(lines):
        while True:
            line = next_line(lines)
            if len(line) == 0:
                continue
            if len(line) == 2:
                data = line[0].split()
                comment = line[1]
            else:
                data = line[0].split()
                comment = None

            if len(data) > 0:
                command = data[0]
                if command == 'M':
                    yield begin_type(lines, data[1], suffix='Msg')
            if comment:
                yield Comment(comment)
    return [*common_parse(iter(text.splitlines()))]


def generate_cpp(elements):
    def generate_type(data):
        texts = [f'class {data.name} {{']
        for field in data.fields:
            name, value_type, comment = field
            if isinstance(value_type, Array):
                value_type = f'std::vector<{value_type.inner_type}>'
            texts.append(f'    {value_type} {name} {generate_comment(comment)}')
        texts.append('};')
        return '\n'.join(texts)

    def generate_comment(comment):
        return f'//{comment.text}' if len(comment.text) > 0 else ''

    ELM_GENERATORS = {
            DataType: generate_type,
            Comment: generate_comment,
            }
    return '\n'.join([ELM_GENERATORS[type(elm)](elm) for elm in elements])


def generate_py(elms):
    print('not yet')
