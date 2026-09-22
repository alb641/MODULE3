from pathlib import Path
from unittest.mock import patch
import runpy

import pytest

from calculator.main import (
    calculate,
    get_number,
    get_operation,
    run_calculator,
)


def test_get_number_with_invalid_input():
    with patch("builtins.input", side_effect=["hello", "5"]):
        result = get_number("Enter number: ")

    assert result == 5.0


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("+", "add"),
        ("add", "add"),
        ("-", "subtract"),
        ("subtract", "subtract"),
        ("*", "multiply"),
        ("multiply", "multiply"),
        ("/", "divide"),
        ("divide", "divide"),
        ("q", None),
        ("quit", None),
    ],
)
def test_get_operation(user_input, expected):
    with patch("builtins.input", return_value=user_input):
        assert get_operation() == expected


def test_get_operation_invalid_then_valid():
    with patch("builtins.input", side_effect=["%", "+"]):
        assert get_operation() == "add"


@pytest.mark.parametrize(
    "operation, expected",
    [
        ("add", 5),
        ("subtract", 1),
        ("multiply", 6),
        ("divide", 1.5),
    ],
)
def test_calculate(operation, expected):
    assert calculate(3, 2, operation) == expected


def test_calculate_invalid_operation():
    with pytest.raises(ValueError, match="Invalid operation."):
        calculate(3, 2, "invalid")


def test_run_calculator():
    user_inputs = ["+", "2", "3", "q"]

    with patch("builtins.input", side_effect=user_inputs):
        run_calculator()


def test_run_calculator_division_by_zero():
    user_inputs = ["/", "10", "0", "q"]

    with patch("builtins.input", side_effect=user_inputs):
        run_calculator()


def test_main_entry_point():
    main_file = Path(__file__).parent.parent / "calculator" / "main.py"

    with patch("builtins.input", side_effect=["q"]):
        runpy.run_path(str(main_file), run_name="__main__")