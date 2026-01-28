from io_lib.output import write_to_file
from matcher_a import matchingEngine
from matcher_b import generateMatchings
from scalability_lib.generator import Generator
from verifier_lib.verifier import match_verifier, stability_verifier


def test_e2e_1():
    runs = 10000

    for i in range(runs):
        n = 8
        generated = Generator(n)
        preferences_a, preferences_b = generated.get_preferences()

        hospital_prefs = {i + 1: preferences_a[i] for i in range(n)}
        student_prefs = {i + 1: preferences_b[i] for i in range(n)}

        # matching = matchingEngine(hospital_prefs, student_prefs, n)
        matching = generateMatchings(n, preferences_a, preferences_b)

        if not match_verifier(matching, n):
            write_to_file(
                "test_output.out", matching, preferences_a, preferences_b, "INVALID"
            )
            assert False

        if not stability_verifier(matching, hospital_prefs, student_prefs):
            write_to_file(
                "test_output.out", matching, preferences_a, preferences_b, "UNSTABLE"
            )
            assert False

        # write_to_file(
        #     "test_output.out", matching, preferences_a, preferences_b, "CORRECT"
        # )
