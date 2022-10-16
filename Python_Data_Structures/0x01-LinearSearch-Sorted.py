"""ALgorithm:
    Linear Search in ascending order
Args:
    Cards: A deck or number of cards to select
    query: The target number or card
    index: The position of the number selected
"""
def search(cards, query):
    index = 0
    while index < len(cards):
        if cards[index] == query:
            return index
        elif cards[index] > query:
            return -1
        index += 1

    return -1
