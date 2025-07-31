def approximate_sqrt(m: float, tol: float = 1e-5) -> float:
    """
    Approximate the square root of a number using iterative formula.

    Args:
        m (float): The number to compute the square root of. Must be positive.
        tol (float): The tolerance level to stop iteration. Default is 1e-5.

    Returns:
        float: Approximate value of the square root of m.

    Raises:
        ValueError: If m is negative.
    """
    if m < 0:
        raise ValueError("Cannot compute square root of a negative number.")

    def next_approximation(x: float) -> float:
        """Compute the next approximation based on the current value."""
        return 0.5 * (x + m / x)

    def is_close_enough(x_new: float, x_old: float) -> bool:
        """Check if the approximation has converged."""
        return abs(x_new - x_old) < tol

    guess = 1.0
    while True:
        new_guess = next_approximation(guess)
        if is_close_enough(new_guess, guess):
            return new_guess
        guess = new_guess
