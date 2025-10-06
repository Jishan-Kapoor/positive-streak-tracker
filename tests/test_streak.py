import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Tests an empty list, expecting 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks_longest_wins():
    """Tests a list with multiple streaks to ensure the longest one is returned."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_with_zeros_and_negatives():
    """Tests that zeros and negative numbers correctly break the streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, -5, 6]) == 2

def test_all_positive_numbers():
    """Tests a list with only positive numbers."""
    assert longest_positive_streak([1, 2, 3]) == 3

def test_all_non_positive_numbers():
    """Tests a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_single_number_streak():
    """Tests a streak of a single number."""
    assert longest_positive_streak([0, 5, 0]) == 1

def test_streak_at_the_beginning():
    """Tests a streak at the beginning of the list."""
    assert longest_positive_streak([5, 6, 7, -1, 8]) == 3

def test_streak_at_the_end():
    """Tests a streak at the end of the list."""
    assert longest_positive_streak([-1, 8, 5, 6, 7]) == 4

def test_from_prompt_1():
    """Test case from prompt: [2, 3, -1, 5, 6, 7, 0, 4] == 3"""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_from_prompt_2():
    """Test case from prompt: [] == 0"""
    assert longest_positive_streak([]) == 0

def test_from_prompt_3():
    """Test case from prompt: [1, 1, 1] == 3"""
    assert longest_positive_streak([1, 1, 1]) == 3