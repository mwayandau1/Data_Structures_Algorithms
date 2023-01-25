def selection_sort(arr):
    size = len(arr)
    for i in range(size-1):
        min_index = i

        for j in range(min_index+1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:

                arr[i], arr[min_index] = arr[min_index], arr[i]
# Selection sort on dictionary
def multilevel_selection_sort(elements, sort_by_list):
    for sort_by in sort_by_list[-1::-1]:
        for x in range(len(elements)):
            min_index = x
            for y in range(x, len(elements)):
                if elements[y][sort_by] < elements[min_index][sort_by]:
                    min_index = y
            if x != min_index:
                elements[x], elements[min_index] = elements[min_index], elements[x]

if __name__ == "__main__":

    # arr = [[2,5,7,9,4,6,7,88,9],
    #        [45,8,90,32,60,1],
    #        [],
    #        [-1,-9],
    #        [0]]
    # for elements in arr:
    #     selection_sort(elements)
    #     print(elements)


    elements = [
        {"name" : "moses", "age": 20},
        {"name": "ab", "age": 23},
        {"name": "aaro", "age": 19},
        {"name": "collins", "age": 21},
        {"name": "bright", "age": 22},

    ]
    multilevel_selection_sort(elements, ["name","age"])
    print(elements)
