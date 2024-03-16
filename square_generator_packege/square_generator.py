class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            return []
        return [x**2 for x in range(start, end + 1)]

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of range must be greater than or equal to start.")
        return [x**2 for x in range(start, end + 1)]

cubic_gen = CubicGenerator()

squares_list = cubic_gen.generate_squares(1, 5)
print(squares_list)