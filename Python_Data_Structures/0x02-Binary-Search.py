#!/usr/bin/python3
"""
Model: Binary search implementation
Args:
    cards:
    A list of cards of cards to be selected
    query:
    the target value
    low: The startiing point of the list
    high: The end point of the list
    mid: Middle of the list
    mid_Value: The middle value selected
    """
def locate_card(cards, query):
    low, high = 0, len(cards) - 1
    while low < high:
        mid = (low + high) // 2
        mid_Value = cards[mid]

       # print("Low :", low, "high :", high, "Middle Value :", mid_Value[mid])
        if mid_Value == query:
            return mid
        elif mid_Value < query:
            high = mid - 1
        elif mid_Value > query:
            low = mid + 1
     return -1
