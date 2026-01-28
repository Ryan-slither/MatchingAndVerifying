def write_to_file(
    file_name: str,
    matchings: dict[int, int],
    preferences_a: list[list[int]] = [],
    preferences_b: list[list[int]] = [],
    context: str = "",
):
    with open(f"./data/{file_name}", "w") as f:
        f.write(
            "".join(
                [f"{hospital} {student}\n" for hospital, student in matchings.items()]
            )
        )
        for prefs in preferences_a:
            f.write(" ".join(map(lambda n: str(n), prefs)) + "\n")
        for prefs in preferences_b:
            f.write(" ".join(map(lambda n: str(n), prefs)) + "\n")
        if context:
            f.write(context + "\n")
