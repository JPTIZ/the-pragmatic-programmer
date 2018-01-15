'''Turtle language module.'''


class ParseError(Exception):
    pass


class InvalidPen(ParseError):
    pass


class InvalidCommand(ParseError):
    pass


class Parser:
    def __init__(self, x=0, y=0):
        self.drawing = False
        self.pen = Parser.PENS[0]
        self.x = x
        self.y = x

    def select_pen(self, number):
        try:
            self.pen = Parser.PENS[int(number)]
        except IndexError:
            raise InvalidPen(f'{number} is not a valid pen')
        print(f'selected pen: {self.pen}')

    def pen_up(self):
        self.drawing = False
        print('pen up')

    def pen_down(self):
        self.drawing = True
        print('pen down')

    def draw_north(self, distance):
        self.move(0, int(distance))

    def draw_east(self, distance):
        self.move(int(distance), 0)

    def draw_south(self, distance):
        self.move(0, -int(distance))

    def draw_west(self, distance):
        self.move(-int(distance), 0)

    def move(self, dx, dy):
        if self.drawing:
            print(f'drew from {self.x, self.y} to {self.x + dx, self.y + dy}')
        else:
            print(f'moved from {self.x, self.y} to {self.x + dx, self.y + dy}')
        self.x += dx
        self.y += dy

    def parse(self, code):
        for line in code.splitlines():
            args = line.split('#')[0].split()

            try:
                command = Parser.COMMANDS[args[0]]
            except KeyError:
                raise InvalidCommand(f'"{args[0]}" is not a valid command')
            command(self, *args[1:])

    COMMANDS = {
            'P': select_pen,
            'D': pen_down,
            'U': pen_up,
            'N': draw_north,
            'E': draw_east,
            'S': draw_south,
            'W': draw_west,
            }

    PENS = [
            'black',
            'white',
            'red',
            'green',
            'blue',
            ]


if __name__ == '__main__':
    print('Welcome to Turtle!')
    parser = Parser()
    try:
        while True:
            code = input('>>> ')
            try:
                parser.parse(code)
            except ParseError as err:
                print(f'Parse error: {err}')
    except EOFError:
        print('Bye bye!')
