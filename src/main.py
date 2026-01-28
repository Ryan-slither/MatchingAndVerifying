import sys

from io_lib.output import write_to_file
from io_lib.parser import Parser
from matcher_a import matchingEngine
from matcher_b import generateMatchings
from scalability_lib.scalability import view_scalability
from verifier_lib.verifier import match_verifier, stability_verifier

N_VALUES = [pow(2, i) for i in range(1, 12)]

if __name__ == "__main__":
    arg_count = len(sys.argv)
    if arg_count != 2:
        raise RuntimeError("Must specify an input file path")

    input_file = sys.argv[1]
    p = Parser()
    p.parse_input_file(input_file)

    n = p.n
    hospital_prefs = {i + 1: p.preferences_a[i] for i in range(n)}
    student_prefs = {i + 1: p.preferences_b[i] for i in range(n)}

    matching = matchingEngine(hospital_prefs, student_prefs, n)
    # matching = generateMatchings(p.n, p.preferences_a, p.preferences_b)

    for h in range(1, n + 1):
        print(h, matching[h])

    write_to_file("output.out", matching)

    if not match_verifier(matching, n):
        print("INVALID")
        sys.exit(1)
    else:
        print("VALID")

    if stability_verifier(matching, hospital_prefs, student_prefs):
        print("STABLE")
    else:
        print("UNSTABLE")
        sys.exit(1)

    view_scalability(N_VALUES)
