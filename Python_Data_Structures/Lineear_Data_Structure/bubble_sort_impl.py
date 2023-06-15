# def bubble_sort( elements):
#     size = len(elements)
#
#     for i in range(size-1):
#         swapped = True
#         for j in range(size-1-i):
#             if elements[j] > elements[j+1]:
#                 temp = elements[j]
#                 elements[j] = elements[j+1]
#                 elements[j+1] = temp
#                 swapped = True
#             if not swapped:
#                 break

def bubble_sort(list):
    size = len(list)-1
    for k in range(size):
        swapped = True
        for i in range(size-k):
            if list[i] > list[i + 1]:
                    temp = list[i]
                    list[i] = list[i +1]
                    list[i + 1] = temp
                    swapped = True
            if not swapped:
                break

def sort_dict(elements, key = None):
    size = len(elements)
    for i in range(size-1):
        swapped = True
        for j in range (size-1-i):
            if elements[j][key] > elements[j+1][key]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp
                swapped = True
            if not swapped:
                break


if __name__ == "__main__":
    arr = [[2, 5, 7, 9, 4, 6, 7, 88, 9],
           [45, 8, 90, 32, 60, 1],
           [],
           [-1, -9],
           [0]]
    for elements in arr:


        bubble_sort(elements)
    # elements = [
    #     {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
    #     {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
    #     {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
    #     {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    # ]
    # sort_dict(elements, key='transaction_amount' )
        print(elements)


