from io_lib.parser import Parser


def test_io_1():
    # 3
    # 1 2 3
    # 2 3 1
    # 2 1 3
    # 2 1 3
    # 1 2 3
    # 1 2 3

    solution = {
        "n": 3,
        "a": [[1, 2, 3], [2, 3, 1], [2, 1, 3]],
        "b": [[2, 1, 3], [1, 2, 3], [1, 2, 3]],
    }

    p = Parser()
    p.parse_input_file("./data/input1.in")

    assert p.n == solution["n"]
    assert p.preferences_a == solution["a"]
    assert p.preferences_b == solution["b"]
