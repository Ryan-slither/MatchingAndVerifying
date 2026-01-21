from random import shuffle


class Generator:
    def __init__(self, n: int):
        self.n = n

    def get_preferences(self):
        return (self.generate_shuffled(), self.generate_shuffled())

    def generate_shuffled(self):
        result: list[list[int]] = []
        for _ in range(self.n):
            nums = list(range(1, self.n + 1))
            shuffle(nums)
            result.append(nums)

        return result
