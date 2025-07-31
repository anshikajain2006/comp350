import builtins
import random
import number_guessing_game  

def test_correct_guess(monkeypatch):
    """
    Simulating guessing the correct number on the first try.
    """
    monkeypatch.setattr(random, "randint", lambda a, b: 42)
    monkeypatch.setattr(builtins, "input", lambda _: "42")

    outputs = []
    monkeypatch.setattr(builtins, "print", outputs.append)

    number_guessing_game.play_guessing_game()

    assert any("Correct!" in line for line in outputs)


def test_incorrect_then_correct_guess(monkeypatch):
    """
    Simulating guessing incorrectly first, then correctly.
    """
    monkeypatch.setattr(random, "randint", lambda a, b: 39)

    inputs = iter(["10", "50", "39"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    outputs = []
    monkeypatch.setattr(builtins, "print", outputs.append)

    number_guessing_game.play_guessing_game()

    assert any("Too low" in line or "Too high" in line for line in outputs)
    assert any("Correct!" in line for line in outputs)


def test_invalid_input_then_correct(monkeypatch):
    """
    Simulating user entering invalid input, then valid input.
    """
    monkeypatch.setattr(random, "randint", lambda a, b: 77)

    inputs = iter(["hello", "253", "77"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    outputs = []
    monkeypatch.setattr(builtins, "print", outputs.append)

    number_guessing_game.play_guessing_game()

    assert any("Invalid input" in line for line in outputs)
    assert any("Correct!" in line for line in outputs)


def test_too_low_feedback(monkeypatch):
    monkeypatch.setattr(random, "randint", lambda a, b: 55)

    inputs = iter(["45", "55"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    outputs = []
    monkeypatch.setattr(builtins, "print", outputs.append)

    number_guessing_game.play_guessing_game()

    assert any("Too low" in line for line in outputs)
    assert any("Correct!" in line for line in outputs)


def test_too_high_feedback(monkeypatch):
    monkeypatch.setattr(random, "randint", lambda a, b: 20)

    inputs = iter(["90", "20"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    outputs = []
    monkeypatch.setattr(builtins, "print", outputs.append)

    number_guessing_game.play_guessing_game()

    assert any("Too high" in line for line in outputs)
    assert any("Correct!" in line for line in outputs)
