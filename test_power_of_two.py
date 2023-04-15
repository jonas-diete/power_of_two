from power_of_two import power_of_two

def test_two_should_return_true():
    assert power_of_two(2) == True
    
def test_three_should_return_false():
    assert power_of_two(3) == False

def test_four_should_return_true():
    assert power_of_two(4) == True

def test_five_should_return_false():
    assert power_of_two(5) == False

def test_six_should_return_false():
    assert power_of_two(6) == False

def test_eight_should_return_true():
    assert power_of_two(8) == True