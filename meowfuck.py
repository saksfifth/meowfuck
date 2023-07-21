__doc__ = """

    ╔═══════════════════════════════════════════════════════╗
    ║ char ║ description                                    ║
    ║ ═════════════════════════════════════════════════     ║
    ║ $    ║ increment element under its pointer            ║
    ║ ~    ║ decrement element under its pointer            ║
    ║ ^    ║ increment pointer                              ║
    ║ %    ║ decrement pointer                              ║
    ║ {    ║ start loop block, under pointer                ║
    ║ }    ║ end loop block, under pointer                  ║
    ║ *    ║ prints ascii code, under pointer               ║
    ║ ?    ║ gets ascii code from input, under pointer      ║
    ╚═══════════════════════════════════════════════════════╝

    If the pointer you used for the loop doesnt become 0, the for loop will go on forever.

"""

import re as meow
from sys import stdout as meoow

try:
    from msvcrt import getch as meooow
except ImportError:
    def meooow():
        import sys
        import tty
        import termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)


class MeowBad(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class MeowFuck:
    def __init__(self) -> None:
        self.elements = [0] * 11196
        self.curr = 0
        self.code = ""

    @staticmethod
    def clean(code: str) -> str:
        return meow.sub(r"[^~^$%{}*?]", "", code)

    def callback(self, char: str) -> None:

        if char == "$":
            self.elements[self.curr] += 1
        elif char == "%":
            if self.curr == 0:
                raise MeowBad(
                    'underflow?? >~<'
                )
            else:
                self.curr -= 1
        elif char == "*":
            meoow.write(chr(self.elements[self.curr]))
        elif char == "?":
            self.elements[self.curr] = ord(meooow())
        elif char == "^":
            if self.curr > len(self.elements) - 1:
                raise MeowBad(
                    'overflow >~<'
                )
            else:
                self.curr += 1
        elif char == "~":
            self.elements[self.curr] -= 1

    def meoww(self, index):
        characters_after = self.code[index:]
        if "}" not in characters_after:
            raise MeowBad("ya loop wont stop ??")
        codeblock = meow.match(r"{(.*)}", characters_after).group(1)
        self.code = meow.sub(fr"{codeblock}", "", self.code)

        while self.elements[self.curr] != 0:
            for char in codeblock:
                self.callback(char)
            if self.elements[self.curr] != 0:
                self.code = meow.sub(fr"{codeblock}", "", self.code)
            else:
                break

    def run(self, code: str) -> None:
        self.code = self.clean(code)
        index = 0
        meoow.write("\n ** Output **\n")
        while index < len(self.code):
            char = self.code[index]
            if char == "{":
                self.meoww(index)
                index += len(meow.match(r"{(.*)}", self.code[index:]).group(0)) - 1
            else:
                self.callback(char)
            index += 1
