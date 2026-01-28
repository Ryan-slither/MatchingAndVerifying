import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from time import perf_counter
import matplotlib.pyplot as plt

from generator import Generator
from matcher_a import matchingEngine
from matcher_b import generateMatchings


n_values = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

times_a = []
times_b = []

for n in n_values:
    prefs_a_list, prefs_b_list = Generator(n).get_preferences()

    hospital_prefs_dict = {i + 1: prefs_a_list[i] for i in range(n)}
    student_prefs_dict = {i + 1: prefs_b_list[i] for i in range(n)}
    
    # runtime for matcher a
    start_a = perf_counter()
    matchingEngine(hospital_prefs_dict, student_prefs_dict, n)
    end_a = perf_counter()

    times_a.append(end_a - start_a)

    #runtime for matcher b
    start_a = perf_counter()
    generateMatchings(n, prefs_a_list, prefs_b_list)
    end_a = perf_counter()

    times_b.append(end_a - start_a)

plt.plot(n_values, times_a, marker="o", label="Matcher A")
plt.plot(n_values, times_b, marker="o", label="Matcher B")

plt.xlabel("n (number of hospitals/students)")
plt.ylabel("Runtime (seconds)")
plt.title("Runtime of Matching Algorithms")
plt.legend()
plt.grid(True)

plt.show()
