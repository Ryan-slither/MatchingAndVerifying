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
    hospitals_match: dict[int, int],
    hospital_prefs: dict[int, list[int]],
    student_prefs: dict[int, list[int]],
):
    # print("Matches:", hospitals_match)
    for hospital, hospital_pref_list in hospital_prefs.items():
        # print("Curr Hospital:", hospital)
        # print("Curr Hospital Pref:", hospital_pref_list)
        for preferred_student in hospital_pref_list:
            if preferred_student == hospitals_match[hospital]:
                break

            for preferred_hospital in student_prefs[preferred_student]:
                # print("Curr Pref Hospital:", preferred_hospital)
                if (
                    preferred_hospital == hospitals_match[hospital]
                    or hospitals_match[preferred_hospital] == preferred_student
                ):
                    break

                if preferred_hospital == hospital:
                    return False

    return True
