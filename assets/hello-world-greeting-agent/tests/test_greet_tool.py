"""Unit tests for the greet tool."""

import pytest
from tools.greet import greet


def test_greet_with_name():
    """greet('Alice') should return 'Hello, Alice!'"""
    result = greet.invoke({"name": "Alice"})
    assert result == "Hello, Alice!"


def test_greet_with_empty_string():
    """greet('') should return 'Hello!'"""
    result = greet.invoke({"name": ""})
    assert result == "Hello!"


def test_greet_with_whitespace_only():
    """greet('   ') should return 'Hello!'"""
    result = greet.invoke({"name": "   "})
    assert result == "Hello!"


def test_greet_with_different_name():
    """greet('Bob') should return 'Hello, Bob!'"""
    result = greet.invoke({"name": "Bob"})
    assert result == "Hello, Bob!"


def test_greet_preserves_name_case():
    """greet should preserve the casing of the name."""
    result = greet.invoke({"name": "alice"})
    assert result == "Hello, alice!"
