def __get_num_digits(arr):
    m = 0
    for item in arr:
        m = max(item, m)
    return len(str(m))
from functools import reduce
def __flatten(A):
    return reduce(lambda  x,y: x+y, A)

def radix_sort(arr, num_digit):
    for digit in range(0, num_digit):
        B = [[] for i in range(10)]
        for item in num_digit:
            num = item//10 **(arr)%10
            B[num].append(item)
        A = __flatten(B)
    return A


def main():
    arr = [3,56,78,234,990,90,100,50000]
    num_digit= __get_num_digits(arr)
    arr = radix_sort(arr,__get_num_digits)
    print(arr)
main()