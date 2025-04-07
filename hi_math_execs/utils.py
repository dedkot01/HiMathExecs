import numpy as np


def matrix_to_latex(matrix: np.ndarray) -> str:
    latex_str = r"\begin{bmatrix}"
    for row in matrix:
        latex_str += "&".join(map(str, row)) + "\\\\\n"
    latex_str += r"\end{bmatrix}"
    return rf"{latex_str}"
