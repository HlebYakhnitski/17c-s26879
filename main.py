def generate_squares(start, end):
    return [x**2 for x in range(start, end + 1)]

example_squares = generate_squares(1, 10)
print(example_squares)