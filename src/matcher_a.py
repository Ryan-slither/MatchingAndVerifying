def  matchingEngine(hospital_prefs, student_prefs, n):
    n = len(hospital_prefs)
    hospitals_match = {h: None for h in range(1, n+1)}
    student_match = {s: None for s in range(1, n+1)}
    next_pref = {h: 0 for h in range(1, n+1)}

    free_hospitals = list(range(1, n+1))

    while free_hospitals:
        h = free_hospitals.pop(0)

        prefs = hospital_prefs[h]
        i = next_pref[h]

        if i>=n:
            continue
        
        s = prefs[i]
        next_pref[h] += 1

        if student_match[s] is None:
            hospitals_match[h] = s
            student_match[s] = h
        else:
            h_old = student_match[s]

            if student_prefs[s][h] < student_prefs[s][h_old]:
                hospitals_match[h] = s
                student_match[s] = h

                hospitals_match[h_old] = None
                free_hospitals.append(h_old)
            else:
                free_hospitals.append(h)

    return hospitals_match
