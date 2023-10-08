from Mean import School
import pytest

@pytest.fixture
def student():
    return School(5)

def test_contructor(student):
    assert student.code_notes == 5
    assert student.note_total == 5
