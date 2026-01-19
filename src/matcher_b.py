def generateMatchings(
    n: int, prefs_arr_a: list[list[int]], prefs_arr_b: list[list[int]]
):
    matchings_h = [0] * n
    matchings_a = [0] * n

    hospitals_arr_b: list[list[int]] = []
    # Preferences array b indexed by hospital to get preference rather than hospital
    for a in prefs_arr_b:
        hospitals_by_preference = [0] * n
        for preference, h in enumerate(a):
            hospitals_by_preference[h - 1] = preference

        hospitals_arr_b.append(hospitals_by_preference)

    for i in range(n):
        h = i + 1
        h_prefs = prefs_arr_a[i]
        for j in range(n):
            match = matchings_h[i]
            a = h_prefs[j]
            h_prime = matchings_a[a - 1]

            if match == a:
                continue

            if h_prime == 0:
                if matchings_h[i] != 0:
                    matchings_a[matchings_h[i] - 1] = 0

                matchings_h[i] = a
                matchings_a[a - 1] = h

            elif hospitals_arr_b[a - 1][h - 1] < hospitals_arr_b[a - 1][h_prime - 1]:
                a_prime = matchings_h[h_prime - 1]
                if a_prime != 0:
                    matchings_a[a_prime - 1] = 0

                matchings_h[h_prime - 1] = 0

                matchings_h[i] = a
                matchings_a[a - 1] = h

        zero_count = 0
        for h in matchings_h:
            if h == 0:
                zero_count += 1

        if zero_count == 0:
            break

    return matchings_h
