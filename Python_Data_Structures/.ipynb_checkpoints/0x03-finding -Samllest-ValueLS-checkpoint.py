"""
Agorithm : Linear search
smallest : The smallet value returrned
squence: The list of numbers to find the smallest in 
i: The counter loop 
Return: The smallest value in the list
    
    """


def searchL(squence):
    smallest = squence[0]
    for i in len(squence):
       if squence[i] < smallest:
            smallest = squence[i]
    return smallest
