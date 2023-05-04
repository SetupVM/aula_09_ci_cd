import methods
import math
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14
    
def test_soma():
    
    x = 10
    y = 10
    
    output = methods.soma(x, y)
    
    assert output == 20 
    
def test_subtracao():
    
    x = 10
    y = 5
    
    output = methods.subtracao(x, y)
    
    assert output == 5
    