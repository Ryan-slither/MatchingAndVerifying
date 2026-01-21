def match_verifier(hospitals_match, hospital_prefs, student_prefs, n):
    if len(hospitals_match) != n:
        return f"ERROR: Hospitals matched do not meet required number of {n} matches"

    for h in hospitals_match:
        if hospitals_match[h] is None:
            return f"ERROR: Hospital {h} remains unmatched"
        
    students = list(hospitals_match.values())

    if len(set(students)) != n:
        return f"ERROR: Set of unique values does not meet required number of {n} matches, indicating duplicate assignments"
    
    for s in students:
        if s > n or s < 1:
            return "ERROR: Invalid pairing of hospital to students as student ID falls out of scope"
