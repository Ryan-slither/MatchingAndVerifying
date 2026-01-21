import sys

from io_lib.parser import Parser
from matcher_b import generateMatchings

if __name__ == "__main__":
    arg_count = len(sys.argv)
    if arg_count != 2:
        raise RuntimeError("Must specify an input file path")

    input_file = sys.argv[1]
    p = Parser()
    p.parse_input_file(input_file)

    print(generateMatchings(p.n, p.preferences_a, p.preferences_b))
