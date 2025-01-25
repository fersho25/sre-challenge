class ShapeArea:

    @staticmethod
    def circle_area(radius, pi=3.14):
        return pi * radius * radius

    @staticmethod
    def square_area(side):
        return side * side

    @staticmethod
    def rectangle_area(height, length):
        return height * length

    @staticmethod
    def triangle_area(base, height):
        return 0.5 * base * height

# Get user inputs with input validation
def get_input(prompt, conversion_func=float, split_char=None):
    while True:
        user_input = input(prompt)
        try:
            if split_char:
                values = user_input.split(split_char)
                return tuple(conversion_func(value) for value in values)
            else:
                return conversion_func(user_input)
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

circle_radius = get_input("Enter circle's radius: ")

square_side = get_input("Enter square's side: ")

rectangle_height, rectangle_length = get_input("Enter height and length for a rectangle (separate by space): ", split_char=" ")

triangle_base, triangle_height = get_input("Enter base and height for a triangle (separate by space): ", split_char=" ")

circle_result = ShapeArea.circle_area(circle_radius)
square_result = ShapeArea.square_area(square_side)
rectangle_result = ShapeArea.rectangle_area(rectangle_height, rectangle_length)
triangle_result = ShapeArea.triangle_area(triangle_base, triangle_height)

print(f"Circle area: {round(circle_result, 2)}")
print(f"Square area: {round(square_result, 2)}")
print(f"Rectangle area: {round(rectangle_result, 2)}")
print(f"Triangle area: {round(triangle_result, 2)}")


