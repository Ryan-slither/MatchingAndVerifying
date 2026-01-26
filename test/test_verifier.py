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
    assert stability_verifier(matchings, hospital_prefs, applicant_prefs, n)

    assert match_verifier(matchings_incorrect, n)
    assert not stability_verifier(
        matchings_incorrect, hospital_prefs, applicant_prefs, n
    )

    assert not match_verifier(matchings_with_holes, n)
