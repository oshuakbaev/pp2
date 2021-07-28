def test_range(n):
    if n in range(2,10):
        print("%s is in range"%str(n))
    else:
        print("number isn't in range")

test_range(4)