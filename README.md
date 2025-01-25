# sre-challenge
Challenge related with the onboarding for SREs

# Assisted by watsonx Code Assistant 
#test.py
class ShapeArea:
    """
    A class to calculate the area of different shapes.

    Methods:
    circle_area(radius, pi=3.14) - Calculate the area of a circle.
    square_area(side) - Calculate the area of a square.
    rectangle_area(height, length) - Calculate the area of a rectangle.
    triangle_area(base, height) - Calculate the area of a triangle.
    """

    @staticmethod
    def circle_area(radius, pi=3.14):
        """
        Calculate the area of a circle.

        Parameters:
        radius (float): The radius of the circle.
        pi (float, optional): The value of pi. Defaults to 3.14.

        Returns:
        float: The area of the circle.
        """
        return pi * radius * radius

    @staticmethod
    def square_area(side):
        """
        Calculate the area of a square.

        Parameters:
        side (float): The length of one side of the square.

        Returns:
        float: The area of the square.
        """
        return side * side

    @staticmethod
    def rectangle_area(height, length):
        """
        Calculate the area of a rectangle.

        Parameters:
        height (float): The height of the rectangle.
        length (float): The length of the rectangle.

        Returns:
        float: The area of the rectangle.
        """
        return height * length

    @staticmethod
    def triangle_area(base, height):
        """
        Calculate the area of a triangle.

        Parameters:
        base (float): The length of the base of the triangle.
        height (float): The height of the triangle.

        Returns:
        float: The area of the triangle.
        """
        return 0.5 * base * height

# Get user inputs with input validation
def get_input(prompt, conversion_func=float, split_char=None):
    """
    Get user input and validate it.

    Parameters:
    prompt (str): The prompt to display to the user.
    conversion_func (function, optional): The function to convert the user input to the desired type. Defaults to float.
    split_char (str, optional): The character to split the user input by. Defaults to None.

    Returns:
    The converted user input.
    """
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
