from main import testing_function

def test_testing_function():
    assert testing_function() == "Im a testing function!"

def test_error():
    assert testing_function() == "ASD"