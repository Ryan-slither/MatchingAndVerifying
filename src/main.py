import sys

from io_lib.parser import Parser
from matcher_b import generateMatchings
from verifier_lib.verifier import match_verifier, stability_verifier


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

    matching = generateMatchings(n, hospital_prefs, student_prefs)

    final_matching = {
        h + 1: (matching[h] + 1 if matching[h] != -1 else -1)
        for h in range(n)
    }


    for h in range(1, n + 1):
        print(h, final_matching[h])

    if not match_verifier(final_matching, n):
        sys.exit(1)

    if stability_verifier(final_matching, hospital_prefs, student_prefs, n):
        print("VALID STABLE")
    else:
        print("UNSTABLE")


