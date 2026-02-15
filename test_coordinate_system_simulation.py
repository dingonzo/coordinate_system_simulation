from coordinate_system_simulation import Point

def test_point_initialization():
    p = Point(10, 20)
    assert p.x == 10
    assert p.y == 20

def test_point_equality():
    p1 = Point(5, 5)
    p2 = Point(5, 5)
    assert p1 == p2 
