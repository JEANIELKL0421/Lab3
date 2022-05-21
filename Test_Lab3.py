import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90,91,92,93]
    test_arr = [11, 12, 22, 25, 34, 64, 90,91,92,93]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90,91,92,93]
    test_arr = [93,92,91,90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_re2():
    result = 2
    input_arr = [1,2]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == 2)

def test_bubble_sort_re3():
    result = 1
    input_arr = [1,2,3,4,5,6,7,8,9,0,1]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == 1)

def test_bubble_sort_re4():
    result = 0
    input_arr = []

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == 0)

def test_bubble_sort_re5():
    result = 3
    input_arr = ['algerbra']

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == 3)

