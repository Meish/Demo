from app import addition, substraction

def test_addition():
    assert(addition(3,4) == 7)
    assert(addition(3,2) == 5)
    assert(addition(0,4) == 4)
    print("test1 - passed")

def test_substraction():
    assert(substraction(3,2) == 1)
    assert(substraction(3,1) == 2)
    print("test2 - passed")

def main():
    test_substraction()
    test_addition()

if __name__ == '__main__':
    main()

