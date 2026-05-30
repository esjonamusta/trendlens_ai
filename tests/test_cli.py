from trendlens_ai.cli import greet


def test_greet():
    assert greet("World") == "Hello, World"
