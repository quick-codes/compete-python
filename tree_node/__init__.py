from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        """
        Returns a list of node values in level-order traversal.
        :return: list of values as string
        """
        nodes = []
        fifo = deque()
        fifo.append(self)

        while fifo:
            current = fifo.popleft()
            nodes.append(current)
            if current:
                fifo.append(current.left)
                fifo.append(current.right)

        while nodes and nodes[-1] is None:
            nodes.pop()
        nodes = [str(node.val) if node else str(None) for node in nodes]
        return '[' + ', '.join(nodes) + ']'


def list_to_binary_tree(nodes):
    """
    Creates binary tree given a list of node values
    :param nodes: list of values
    :return: root of the binary tree
    """
    nodes = [TreeNode(node) if node is not None else None for node in nodes]
    right = 0
    for ind in range(len(nodes)):
        if nodes[ind] is None:
            continue

        left = right + 1
        if left < len(nodes):
            nodes[ind].left = nodes[left]

        right = left + 1
        if right < len(nodes):
            nodes[ind].right = nodes[right]
    return nodes[0] if len(nodes) > 0 else None
