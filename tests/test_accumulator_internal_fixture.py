from pages.accumulator import Accumulator
import pytest

@pytest.fixture
def accum():
    return Accumulator()


def test_accum_creation(accum):
    assert accum.count == 0


def test_add_counts_twice():
    accum = Accumulator()
    accum.add_counts()
    accum.add_counts()
    assert accum.count == 2

def test_add_counts_with_params():
    accum = Accumulator(10)
    assert accum.count == 10