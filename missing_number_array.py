def missing_array(arr, n, low, high):
 
    # Insert all elements of
    # arr[] in set
    s = set(arr)
 

    for x in range(low, high + 1):
        if x not in s:
            print(x, end = ' ')
 
if __name__ == '__main__':
    # operation 
    input_arr = [0, 1, 3, 50, 75]
    #input_arr = input("input array")
    n = len(input_arr)
    low_range = int(input("Please Enter lower range"))
    high_range = int(input("please Enter higher range"))

    missing_array(input_arr, n, low_range, high_range)
 
