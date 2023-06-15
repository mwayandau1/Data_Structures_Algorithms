
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    left=merge_sort(left)
    right=merge_sort(right)

    return sorted_two_merge(left, right)

def sorted_two_merge(a, b):
    len_a = len(a)
    len_b = len(b)
    i =j = 0
    sorted_list = []

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i = i+1
        else:
            sorted_list.append(b[j])
            j += 1
    while i < len_a:
        sorted_list.append(a[i])
        i += 1
    while j < len_b:
        sorted_list.append(a[j])
        j += 1
    return sorted_list












if __name__ == "__main__":
    arr = [5,6,8, 2,60, 50,70,30,10,12]
    print(merge_sort(arr))