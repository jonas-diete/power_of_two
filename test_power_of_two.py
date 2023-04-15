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

def test_sixteen_should_return_true():
    assert power_of_two(16) == True

def test_thirtytwo_should_return_true():
    assert power_of_two(32) == True

def test_thousandtwentyfour_should_return_true():
    assert power_of_two(1024) == True

def test_fourthousandninetysix_return_true():
    assert power_of_two(4096) == True

def test_eightthousandonehundredninetytwo_return_true():
    assert power_of_two(8192) == True

def test_fifty_return_true():
    assert power_of_two(50) == False

def test_threethousand_return_true():
    assert power_of_two(3000) == False

def test_hundredandtwentyseven_return_true():
    assert power_of_two(127) == False