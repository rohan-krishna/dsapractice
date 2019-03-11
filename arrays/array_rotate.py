# for the sake of simplicity, we'll use python list
# this is also known as Left Shifting of Arrays
def rotateArray(arr, d):
    # arr = the input array
    # d = number of rotations
    shift_elements = arr[0:d]
    arr[:d] = []
    arr.extend(shift_elements)
    return arr

if __name__ == "__main__":
    print("How many time do you want to shift the array: ")
    n = int(input())

    print("Enter Array (e.g: 1 2 3 == [1,2,3]): ")
    arr = list(map(int, input().rstrip().split()))

    res = rotateArray(arr, n)
    print(res)