#!/usr/bin/env python3

from calendar import TUESDAY, WEDNESDAY
from http.client import REQUEST_HEADER_FIELDS_TOO_LARGE
import io
from typing import Tuple
import sys

iota_counter = 0


def iota(reset=False):
    global iota_counter
    if reset:
        iota_counter = 0
    result = iota_counter
    iota_counter += 1
    return result


OP_PUSH = iota(True)
OP_PLUS = iota()
OP_DUMP = iota()
OP_MINUS = iota()
OP_COUNTS = iota()

# print("OP_PUSH", OP_PUSH)
# print("OP_PLUS", OP_PLUS)
# print("OP_DUMP", OP_DUMP)
# print("OP_COUNTS", OP_COUNTS)


def push(x):
    return (OP_PUSH, x)


def plus():
    return (OP_PLUS, )


def minus():
    return (OP_MINUS, )


def dump():
    return (OP_DUMP, )


def simulate_program(program):
    assert OP_COUNTS == 4, "Exhaustive Handling of Operations in simulation"
    command_stack = []
    for op in program:
        if op[0] == OP_PUSH:
            command_stack.append(op[1])
        elif op[0] == OP_PLUS:
            command_stack.append(command_stack.pop()+command_stack.pop())
        elif op[0] == OP_MINUS:
            command_stack.append(-command_stack.pop()+command_stack.pop())
        elif op[0] == OP_DUMP:
            print(command_stack.pop())
        else:
            assert False, "Unreachable"


def compile_program(program):
    assert False, "Not Implemented"


program = [
    push(4),
    push(5),
    plus(),
    dump(),
    push(100),
    push(30),
    minus(),
    dump(),
    push(55),
    dump()
]



def usage():
    print("Usage: sosta <SUBCOMMAND> [AGRS]")
    print("   com        Compile The Program")
    print("   sim        Simulate The Program")
    print("SUBCOMMANDS: ")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        print("ERROR: No Subcommand Is Provided")
        exit(1)

    subcommand = sys.argv[1]
    if subcommand == "sim":
        simulate_program(program)
    elif subcommand == "com":
        compile_program(program)
    else:
        usage()
        print("ERROR:  Unknown Subcommand %s" % (subcommand))
        exit(1)
