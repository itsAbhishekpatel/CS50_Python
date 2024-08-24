from t32 import square

# assert keyword - check if something ture or not
def main():
    test_square()
    

def test_square():
    if square(2) != 4:
        print("2 square was not 4")
    if square(5) != 25:
        print("5 square was not 25")
    try:
        assert square(10) == 100
    except AssertionError:
        print("10 square was not 100")
if __name__ == "__main__":
    main()
    print("Pass all test cases!")

# so there is tool called pytest program so you do not write everthing to test your code 
# unit test typically test individual modules or funcitons 