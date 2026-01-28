from time import perf_counter

import matplotlib.pyplot as plt

from matcher_a import matchingEngine
from matcher_b import generateMatchings
from scalability_lib.generator import Generator
from verifier_lib.verifier import match_verifier, stability_verifier


def view_scalability(n_values):
    times_a = []
    times_b = []
    times_c = []

    for n in n_values:
        prefs_a_list, prefs_b_list = Generator(n).get_preferences()

        hospital_prefs_dict = {i + 1: prefs_a_list[i] for i in range(n)}
        student_prefs_dict = {i + 1: prefs_b_list[i] for i in range(n)}

        # runtime for matcher a
        total_time_a = 0
        matching_a: dict[int, int] = {}
        for _ in range(3):
            start_a = perf_counter()
            matching_a = matchingEngine(hospital_prefs_dict, student_prefs_dict, n)
            end_a = perf_counter()
            total_time_a += end_a - start_a

        times_a.append(total_time_a / 3)

        # runtime for matcher b
        total_time_b = 0
        matching_b: dict[int, int] = {}
        for _ in range(3):
            start_b = perf_counter()
            matching_b = generateMatchings(n, prefs_a_list, prefs_b_list)
            end_b = perf_counter()
            total_time_b += end_b - start_b

        times_b.append(total_time_b / 3)

        # runtime for verifier
        total_time_c = 0

        # For Matcher A
        start_c = perf_counter()
        match_verifier(matching_a, n)
        stability_verifier(matching_a, hospital_prefs_dict, student_prefs_dict)
        end_c = perf_counter()
        total_time_c += end_c - start_c

        # For Matcher B
        start_c = perf_counter()
        match_verifier(matching_b, n)
        stability_verifier(matching_b, hospital_prefs_dict, student_prefs_dict)
        end_c = perf_counter()
        total_time_c += end_c - start_c

        times_c.append(total_time_c / 2)

    # print(times_a, times_b, times_c)

    plt.plot(n_values, times_a, marker="o", label="Matcher A")
    plt.plot(n_values, times_b, marker="o", label="Matcher B")
    plt.plot(n_values, times_c, marker="o", label="Verifier")

    plt.xlabel("n (number of hospitals/students)")
    plt.ylabel("Runtime (seconds)")
    plt.title("Runtime of Matching Algorithms & Verifier vs. n")
    plt.legend()
    plt.grid(True)

    plt.show()
