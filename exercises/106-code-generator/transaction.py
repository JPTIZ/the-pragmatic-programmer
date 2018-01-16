'''Database transaction module.'''
import re
from typing import List

from carl import command

from languages import templates as lang_templates


def parse(text, lang):
    print(f'generating for {lang}:')
    lang = lang_templates[lang]

    def next_line(lines):
        return next(lines).split('#', maxsplit=1)

    def begin_type(lines, name, suffix=''):
        type_def = {
                'name': f'{name}{suffix}',
                'fields': {},
                }
        return '\n'.join([
            lang['type-def']['begin'].format(type_name=type_def['name']),
            *parse_fields(lines, type_def),
            lang['type-def']['end'].format(type_name=type_def['name'])])

    def parse_fields(lines, type_def):
        def format_field(field_type):
            def to_array(field_type):
                match = re.compile('([a-zA-Z0-9]+)\[(\d*)\]').match(
                                   field_type)
                if match:
                    return match.groups()
                return None

            array = to_array(field_type)
            if array:
                inner_type = lang['types'][array[0]]
                if len(array[1]) > 0:
                    size = int(array[1])
                    return lang['types']['array'].format(
                            inner_type=inner_type,
                            size=size)
                return lang['types']['vector'].format(
                        inner_type=inner_type)

            if field_type not in lang['types']:
                return field_type
        while True:
            line = next_line(lines)[0].split()
            command = line[0]
            if command == 'E':
                return
            elif command == 'F':
                field_name, field_type = line[1:]
                type_def['fields'][field_name] = {'type': field_type}
                yield ' '*4 + lang['type-def']['field'].format(
                    field_name=field_name,
                    field_type=format_field(field_type))

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
                yield lang['line-comment'].format(comment=comment)
    return '\n'.join([*common_parse(iter(text.splitlines()))])


@command
def main():
    print('main')


@main.subcommand
def gen(input: str,
        languages: List[str]=[]):
    print(f'input file: {input}')
    with open(input) as file:
        input = file.read()
        for lang in 'cpp', 'py':
            print(parse(input, lang))


if __name__ == '__main__':
    main.run()
