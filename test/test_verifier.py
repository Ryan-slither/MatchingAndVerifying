from verifier_lib.verifier import match_verifier, stability_verifier


def test_verifier_1():
    n = 4

    hospital_prefs = {
        1: [1, 2, 3, 4],
        2: [2, 3, 4, 1],
        3: [3, 4, 1, 2],
        4: [4, 1, 2, 3],
    }

    applicant_prefs = {
        1: [3, 4, 1, 2],
        2: [1, 3, 2, 4],
        3: [2, 1, 3, 4],
        4: [4, 2, 3, 1],
    }

    matchings = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
    }

    matchings_incorrect = {
        1: 2,
        2: 1,
        3: 3,
        4: 4,
    }

    matchings_with_holes = {
        1: 1,
        2: None,
        3: 3,
        4: None,
    }

    assert match_verifier(matchings, n)
    assert stability_verifier(matchings, hospital_prefs, applicant_prefs)

    assert match_verifier(matchings_incorrect, n)
    assert not stability_verifier(matchings_incorrect, hospital_prefs, applicant_prefs)

    assert not match_verifier(matchings_with_holes, n)


def test_verifier_2():
    n = 3

    hospital_prefs = {
        1: [1, 2, 3],
        2: [2, 3, 1],
        3: [2, 1, 3],
    }

    applicant_prefs = {
        1: [2, 1, 3],
        2: [1, 2, 3],
        3: [1, 2, 3],
    }

    matchings = {
        1: 1,
        2: 3,
        3: 2,
    }

    assert match_verifier(matchings, n)
    assert not stability_verifier(matchings, hospital_prefs, applicant_prefs)


def test_verifier_3():
    n = 3

    hospital_prefs = {
        1: [1, 2, 3],
        2: [3, 1, 2],
        3: [1, 2, 3],
    }

    applicant_prefs = {
        1: [3, 1, 2],
        2: [1, 2, 3],
        3: [2, 1, 3],
    }

    matchings = {
        1: 2,
        2: 3,
        3: 1,
    }

    assert match_verifier(matchings, n)
    assert stability_verifier(matchings, hospital_prefs, applicant_prefs)
