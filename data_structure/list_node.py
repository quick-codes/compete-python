class ListNode:
    def __init__(self, val=0, next=None, items=None):
        if items is not None:
            if len(items) > 0:
                head = None
                for item in reversed(items):
                    head = ListNode(item, head)
                self.val = head.val
                self.next = head.next
        else:
            self.val = val
            self.next = next

    def __str__(self):
        nodes = []
        current = self
        while current:
            nodes.append(str(current.val))
            current = current.next
        return '[' + ', '.join(nodes) + ']'
