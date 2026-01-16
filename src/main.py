def  matchingEngine(hospital_prefs, student_prefs):
    n = len(hospital_prefs)
    hospitals_matched = [-1] * n
    student_next_pref = [] * n

    hospital_ranks = [[0] * n for _ in range(n)]
    for hospitals in range(n):
        for rank, students in enumerate(hospital_prefs[hospitals]):
            hospital_ranks[hospitals][students] = rank





