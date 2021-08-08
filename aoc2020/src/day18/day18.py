import antlr4

from src.common.util import read_input

from day18_p1Listener import day18_p1Listener
from day18_p1Lexer import day18_p1Lexer
from day18_p1Parser import day18_p1Parser

from day18_p2Listener import day18_p2Listener
from day18_p2Lexer import day18_p2Lexer
from day18_p2Parser import day18_p2Parser


class ExprPartOneListener(day18_p1Listener):
    stack = []

    def exitExprOp(self, ctx: day18_p1Parser.ExprOpContext):
        rhs = self.stack.pop()
        lhs = self.stack.pop()

        if ctx.op.type == day18_p1Lexer.ADD:
            self.stack.append(rhs + lhs)
        elif ctx.op.type == day18_p1Lexer.MULT:
            self.stack.append(rhs * lhs)

    def enterExprInt(self, ctx):
        self.stack.append(int(ctx.getText()))


class ExprPartTwoListener(day18_p2Listener):
    stack = []

    def exitExprAdd(self, ctx: day18_p2Parser.ExprAddContext):
        rhs = self.stack.pop()
        lhs = self.stack.pop()

        self.stack.append(rhs + lhs)
    
    def exitExprMult(self, ctx: day18_p2Parser.ExprMultContext):
        rhs = self.stack.pop()
        lhs = self.stack.pop()

        self.stack.append(rhs * lhs)

    def enterExprInt(self, ctx):
        self.stack.append(int(ctx.getText()))


def part_one(input):
    result = 0

    for expr in input:
        lexer = day18_p1Lexer(antlr4.InputStream(expr))
        parser = day18_p1Parser(antlr4.CommonTokenStream(lexer))
        tree = parser.expr()
        listener = ExprPartOneListener()
        walker = antlr4.ParseTreeWalker()
        walker.walk(listener, tree)
        result += listener.stack.pop()

    return result


def part_two(input):
    result = 0

    for expr in input:
        lexer = day18_p2Lexer(antlr4.InputStream(expr))
        parser = day18_p2Parser(antlr4.CommonTokenStream(lexer))
        tree = parser.expr()
        listener = ExprPartTwoListener()
        walker = antlr4.ParseTreeWalker()
        walker.walk(listener, tree)
        result += listener.stack.pop()

    return result


def main():
    print('Day 18: Answer for Part 1 {}'.format(
        part_one(read_input('inputs/input_day18.txt', '\n'))))
    print('Day 18: Answer for Part 2: {}'.format(
        part_two(read_input('inputs/input_day18.txt', '\n'))))


if __name__ == "__main__":
    main()
