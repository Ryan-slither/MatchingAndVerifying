from collections import deque


def generateMatchings(
    n: int, prefs_arr_a: list[list[int]], prefs_arr_b: list[list[int]]
):
    hospital_pairs = [-1] * n
    applicant_pairs = [-1] * n

    hospitals_arr_b: list[list[int]] = []
    # Preferences array b indexed by hospital to get preference rather than hospital
    for a in prefs_arr_b:
        hospitals_by_preference = [0] * n
        for preference, h in enumerate(a):
            hospitals_by_preference[h - 1] = preference

        hospitals_arr_b.append(hospitals_by_preference)

    pairs: dict[int, deque[int]] = dict()
    for hospital, hospital_prefs in enumerate(prefs_arr_a):
        possible_pairs = deque()
        for applicant in hospital_prefs:
            possible_pairs.append(applicant)

        pairs[hospital] = possible_pairs

    matched = 0
    hospital = 0
    while matched < n:
        if hospital >= n:
            hospital = 0

        if len(pairs[hospital]) == 0:
            hospital += 1
            continue

        applicant = pairs[hospital].popleft() - 1
        print(applicant)

        if applicant_pairs[applicant] == -1:
            print("initial")
            past_applicant = hospital_pairs[hospital]
            if past_applicant != -1:
                applicant_pairs[hospital_pairs[hospital]] = -1
            else:
                matched += 1

            hospital_pairs[hospital] = applicant
            applicant_pairs[applicant] = hospital

        elif (
            hospitals_arr_b[applicant][hospital]
            < hospitals_arr_b[applicant][applicant_pairs[applicant]]
        ):
            print("switched")
            if (
                hospital_pairs[applicant_pairs[applicant]] != -1
                and hospital_pairs[hospital] != -1
            ):
                matched -= 1

            applicant_pairs[hospital_pairs[hospital]] = -1
            hospital_pairs[applicant_pairs[applicant]] = -1
            hospital_pairs[hospital] = applicant
            applicant_pairs[applicant] = hospital

        hospital += 1

        print(pairs)
        print(hospital_pairs)
        print(applicant_pairs)
        print()

    return hospital_pairs
