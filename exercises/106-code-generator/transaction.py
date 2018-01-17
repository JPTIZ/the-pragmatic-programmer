'''Database transaction module.'''
from carl import command

from generators import generate_cpp, generate_py
from parser import parse


@command
def main():
    pass


@main.subcommand
def gen(input: str,
        languages: str='cpp,py'):
    GENERATORS = {
            'cpp': generate_cpp,
            'py': generate_py,
            }
    print(f'input file: {input}')
    with open(input) as file:
        mid = parse(file.read())
    for lang in languages.split(','):
        print(f'\n{"-"*40}\ngenerating for {lang}...')
        print(GENERATORS[lang](mid))


if __name__ == '__main__':
    main.run()
