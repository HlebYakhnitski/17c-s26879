class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            return []
        return [x**2 for x in range(start, end + 1)]

class CubicGenerator(SquareGenerator):
    def generate_cubes(self, start, end):
        if end < start:
            return []
        return [x**3 for x in range(start, end + 1)]

cubic_gen = CubicGenerator()

cubes_list = cubic_gen.generate_cubes(1, 5)
print(cubes_list)