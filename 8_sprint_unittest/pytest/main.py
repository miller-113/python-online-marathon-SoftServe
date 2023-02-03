import pytest

@pytest.fixture
def data():

    return [3, 2, 1, 5]

def test_sel_sort(data):

    sorted_vals = [1, 2, 3, 5]
    
    assert sorted_vals == sorted(data)

if __name__ == '__main__':
    test_sel_sort()