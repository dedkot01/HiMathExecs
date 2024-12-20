import sys

import numpy as np


def generate_matrix_and_determinant(size: int) -> tuple[np.ndarray, int]:
    matrix = np.random.randint(-9, 10, (size, size))
    determinant = round(np.linalg.det(matrix))

    return matrix, determinant


def matrix_to_latex(matrix: np.ndarray) -> str:
    latex_str = r"\begin{bmatrix}"
    for row in matrix:
        latex_str += "&".join(map(str, row)) + "\\\\\n"
    latex_str += r"\end{bmatrix}"
    return rf"{latex_str}"


if __name__ == "__main__":
    difficulty: str = sys.argv[1]

    difficultys = {
        "easy": 2,
        "medium": 3,
        "hard": 4,
    }
    size = difficultys[difficulty]

    matrix, determinant = generate_matrix_and_determinant(size)

    print(
        f"$${matrix_to_latex(matrix)}$$"
        f"<details><summary>Answer</summary><p>{determinant}</p></details>"
    )
