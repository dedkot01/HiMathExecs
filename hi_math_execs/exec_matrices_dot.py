from typing import Annotated

import numpy as np
import typer

from hi_math_execs.constants import Difficulty
from hi_math_execs.utils import matrix_to_latex

app = typer.Typer()


def generate_two_matrices(size: int) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng()

    max_size = max(size, 2)
    min_size = rng.integers(
        low=max(size - 1, 1),
        high=max_size,
        endpoint=True,
    )
    matrices = rng.integers(
        low=-9,
        high=10,
        size=(2, min_size, max_size),
    )

    return matrices[0], matrices[1].T


@app.command()
def cli(
    difficulty: Annotated[
        Difficulty,
        typer.Option(help="Сложность задачи"),
    ] = Difficulty.HARD,
) -> None:
    """Сгенерировать задачу умножения двух матриц в формате LaTeX
    """
    difficultys = {
        Difficulty.EASY: 2,
        Difficulty.MEDIUM: 3,
        Difficulty.HARD: 4,
    }
    size = difficultys[difficulty]

    matrices = generate_two_matrices(size)
    answer: np.ndarray = np.linalg.multi_dot(matrices)

    print(
        f"$$A = {matrix_to_latex(matrices[0])}$$"
        f"$$B = {matrix_to_latex(matrices[1])}$$"
        f"<details><summary>Answer</summary><p>{answer.tolist()}</p></details>",
    )


if __name__ == "__main__":
    app()
