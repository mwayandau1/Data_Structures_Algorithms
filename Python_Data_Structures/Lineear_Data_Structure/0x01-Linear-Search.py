"""
ALgorithm:
    Linear Search
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
        index += 1

    return -1
