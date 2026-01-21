from scalability_lib.generator import Generator


def test_generator_1():
    n_list: list[int] = []
    prev = 1
    for _ in range(10):
        n_list.append(prev)
        prev *= 2

    for n in n_list:
        prefs_a, prefs_b = Generator(n).get_preferences()
        assert len(prefs_a) == n
        assert len(prefs_b) == n

        for pref_list in prefs_a:
            length = len(pref_list)
            assert length == n
            assert len(set(pref_list)) == length

        for pref_list in prefs_b:
            length = len(pref_list)
            assert length == n
            assert len(set(pref_list)) == length
