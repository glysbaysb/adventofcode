INTEGER, PLUS, EOF, MULTIPLY, PAR_OPEN, PAR_CLOSE = \
    'INTEGER', 'PLUS', 'EOF', 'MULTIPLY', '(', ')'

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

class Lexer(object):
    def __init__(self, expr):
        self.expr = expr
        self.pos = 0
        self.current_char = self.expr[self.pos]

    def error(self):
        raise Exception('Error parsing input')

    def advance(self):
        self.pos += 1
        if self.pos >= len(self.expr):
            self.current_char = None
        else:
            self.current_char = self.expr[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        number = ''
        while self.current_char is not None and self.current_char.isdigit():
            number += self.current_char
            self.advance()
        return int(number)

    def get_next_token(self):
        """Lexical analyzer"""
        while self.current_char is not None:
            # skip whitespace
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            # "real" tokens
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())
            elif self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')
            elif self.current_char == '*':
                self.advance()
                return Token(MULTIPLY, '*')
            elif self.current_char == '(':
                self.advance()
                return Token(PAR_OPEN, '(')
            elif self.current_char == ')':
                self.advance()
                return Token(PAR_CLOSE, ')')

            self.error()
        return Token(EOF, None)

class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        # compare current token type with the expected one.
        # if they match, advance
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception("current token is {cur} but expected {exp}".format(cur = self.current_token.type, exp=token_type))

    def term(self):
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return token.value
        elif token.type == PAR_OPEN:
            self.eat(PAR_OPEN)
            tmp = self.parse()
            self.eat(PAR_CLOSE)
            return tmp
        else:
            raise Exception("unknown type {type}".format(type=token))

    def parse(self):
        left = self.term()
        while self.current_token.type in (PLUS, MULTIPLY):
            if self.current_token.type == PLUS:
                self.eat(self.current_token.type)
                left = left + self.term()
            else:
                self.eat(self.current_token.type)
                left = left * self.term()
        return left


if __name__ == '__main__':
    # part 1
    total = 0
    for line in open('input'):
        lexer = Lexer(line)
        total += Parser(lexer).parse()
    print(total)