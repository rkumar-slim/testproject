# tests/test_lib.py
from mlproject.lib import try_me


def test_try_me():
    assert try_me(48.865070, 2.380009, 48.235070,
                     2.393409) == 70.00789153218594
