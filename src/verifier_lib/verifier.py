def match_verifier(hospitals_match, n):
    if len(hospitals_match) != n:
        print(f"ERROR: Hospitals matched do not meet required number of {n} matches")
        return False

    for h in hospitals_match:
        if hospitals_match[h] is None:
            print(f"ERROR: Hospital {h} remains unmatched")
            return False

    students = list(hospitals_match.values())

    if len(set(students)) != n:
        print(
            f"ERROR: Set of unique values does not meet required number of {n} matches, indicating duplicate assignments"
        )
        return False

    for s in students:
        if s > n or s < 1:
            print(
                "ERROR: Invalid pairing of hospital to students as student ID falls out of scope"
            )
            return False

    return True


def stability_verifier(
    hospitals_match: dict[int, int], hospital_prefs, student_prefs, n
):
    for hospital, applicant in hospitals_match.items():
        h_set = set()
        a_set = set()
        h_prefs = hospital_prefs[hospital]
        a_prefs = student_prefs[applicant]

        for h_pref in h_prefs:
            if h_pref == applicant:
                break

            h_set.add(h_pref)

        for a_pref in a_prefs:
            if a_pref == hospital:
                break

            a_set.add(a_pref)

        if len(a_set.intersection(h_set)) != 0:
            return False

    return True
