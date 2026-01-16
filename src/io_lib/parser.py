class Parser:
    def __init__(self):
        self.n = None
        self.preferences_a = None
        self.preferences_b = None

    def parse_input_file(self, file_name: str):
        with open(file_name, "r") as file:
            lines = file.readlines()
            if len(lines) == 0:
                raise RuntimeError("Empty file cannot be parsed")

            self.n = int(lines[0].strip())
            if self.n == 0:
                raise RuntimeError("Cannot match with 0 parties")

            size = self.n + 1
            slice_a = lines[1:size]
            self.preferences_a = self.parse_preferences(slice_a)

            slice_b = lines[size : size + self.n]
            self.preferences_b = self.parse_preferences(slice_b)

    def parse_preferences(self, lines: list[str]):
        preferences_list = []
        for line in lines:
            line_preferences = line.strip().split()
            if len(line_preferences) != self.n:
                raise RuntimeError(f"Row does not have {self.n} entries")

            preferences_list.append(list(map(int, line_preferences)))

        return preferences_list
