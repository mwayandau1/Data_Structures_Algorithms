def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j-1
            elements[j+1] = anchor


if __name__ == "__main__":
    el = [
        [5,2,9,1,0,-34,-100],
        [],
        [1,3,5,7,9],
        [3]

    ]
    for elements in el:
        insertion_sort(elements)
        print(elements)