def count_ocurrences_singly_linked(self, node, data):
    if node is None:
        return 0
    if node.data == data:
        return 1 + self.count_ocurrences_singly_linked(node.next, data)
    else:
        return self.count_occurrences_singly_linked(node.next, data)