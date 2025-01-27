# SRE Challenge

## Overview

This repository is part of the **Site Reliability Engineering (SRE) Onboarding Challenge**. It includes a Python class designed to calculate the area of various geometric shapes, serving as a practical exercise in software development and mathematical computations.

---

## Features

- **ShapeArea Class:** A Python class with static methods to compute the area of:
  - Circles
  - Squares
  - Rectangles
  - Triangles

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Methods](#methods)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

---

## Installation

### Prerequisites

- Python 3.6 or higher installed on your system.

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/fersho25/sre-challenge.git
   cd sre-challenge
   ```

2. **Set Up a Virtual Environment (Optional but Recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   - If there are any dependencies, install them using:
     ```bash
     pip install -r requirements.txt
     ```

---

## Usage

1. **Navigate to the Project Directory:**
   ```bash
   cd sre-challenge
   ```

2. **Import the ShapeArea Class:**
   - In your Python script or interactive shell, import the class:
     ```python
     from shape_area import ShapeArea
     ```

3. **Calculate Areas:**
   - Use the static methods to calculate areas:
     ```python
     # Calculate the area of a circle with radius 5
     circle_area = ShapeArea.circle_area(5)

     # Calculate the area of a square with side length 4
     square_area = ShapeArea.square_area(4)

     # Calculate the area of a rectangle with height 3 and length 6
     rectangle_area = ShapeArea.rectangle_area(3, 6)

     # Calculate the area of a triangle with base 8 and height 5
     triangle_area = ShapeArea.triangle_area(8, 5)
     ```

---

## Methods

### `circle_area(radius, pi=3.14)`

- **Description:** Calculates the area of a circle.
- **Parameters:**
  - `radius` (float): The radius of the circle.
  - `pi` (float, optional): The value of π (pi). Defaults to 3.14.
- **Returns:** `float` - The area of the circle.

### `square_area(side)`

- **Description:** Calculates the area of a square.
- **Parameters:**
  - `side` (float): The length of one side of the square.
- **Returns:** `float` - The area of the square.

### `rectangle_area(height, length)`

- **Description:** Calculates the area of a rectangle.
- **Parameters:**
  - `height` (float): The height of the rectangle.
  - `length` (float): The length of the rectangle.
- **Returns:** `float` - The area of the rectangle.

### `triangle_area(base, height)`

- **Description:** Calculates the area of a triangle.
- **Parameters:**
  - `base` (float): The base length of the triangle.
  - `height` (float): The height of the triangle.
- **Returns:** `float` - The area of the triangle.

---

## Testing

To ensure the methods work correctly, you can write unit tests using Python's built-in `unittest` framework or any other testing framework of your choice.

1. **Create a Test File:**
   - Create a file named `test_shape_area.py` in the project directory.

2. **Write Test Cases:**
   - Write test cases for each method in the `ShapeArea` class.

3. **Run Tests:**
   ```bash
   python -m unittest test_shape_area.py
   ```

---

## Contributing

We welcome contributions to enhance this project! To contribute:

1. **Fork the Repository:** Click the "Fork" button at the top-right corner of this page.
2. **Clone Your Fork:**
   ```bash
   git clone https://github.com/<your-username>/sre-challenge.git
   cd sre-challenge
   ```
3. **Create a Feature Branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Commit Your Changes:**
   ```bash
   git add .
   git commit -m "Add your feature description"
   ```
5. **Push Your Branch:**
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Submit a Pull Request:** Go to your forked repository, click "Compare & pull request," and describe your changes.

---

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this project under the terms of the license.

---

## Contact

For questions, suggestions, or feedback, feel free to open an issue or contact the repository owner.

---