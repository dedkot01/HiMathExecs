from typing import Annotated

import numpy as np
import typer

from hi_math_execs.constants import Difficulty

app = typer.Typer()


def generate_matrix_and_determinant(size: int) -> tuple[np.ndarray, int]:
    matrix = np.random.default_rng().integers(
        low=-9,
        high=10,size=(size, size),
    )
    determinant = round(np.linalg.det(matrix))

    return matrix, determinant


def matrix_to_latex(matrix: np.ndarray) -> str:
    latex_str = r"\begin{bmatrix}"
    for row in matrix:
        latex_str += "&".join(map(str, row)) + "\\\\\n"
    latex_str += r"\end{bmatrix}"
    return rf"{latex_str}"


@app.command()
def cli(
    difficulty: Annotated[
        Difficulty,
        typer.Option(help="Сложность задачи"),
    ] = Difficulty.HARD,
) -> None:
    """Сгенерировать задачу нахождения определителя матрицы в формате LaTeX
    """
    difficultys = {
        Difficulty.EASY: 2,
        Difficulty.MEDIUM: 3,
        Difficulty.HARD: 4,
    }
    size = difficultys[difficulty]

    matrix, determinant = generate_matrix_and_determinant(size)

    print(
        f"$${matrix_to_latex(matrix)}$$"
        f"<details><summary>Answer</summary><p>{determinant}</p></details>",
    )


if __name__ == "__main__":
    app()
