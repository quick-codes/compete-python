class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        nodes = []
        current = self
        while current:
            nodes.append(str(current.val))
            current = current.next
        return '[' + ', '.join(nodes) + ']'


def list_to_linked_list(items):
    head = None
    for item in reversed(items):
        head = ListNode(item, head)
    return head
