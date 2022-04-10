class SegmentTree:
    def __init__(self, offset):
        """
        Segment tree for calculating prefix frequency
        :param offset:
        """
        self.offset = offset
        self.leaves = 2 * self.offset + 1
        self.tree = [0 for _ in range(2 * self.leaves)]

    def query(self, limit):
        result = 0
        left = self.leaves
        right = limit + self.offset + self.leaves

        while left < right:
            if left % 2 == 1:
                # left nodes are ignored to add the parent instead to cover left and right
                result += self.tree[left]
                left += 1
            left //= 2
            if right % 2 == 1:
                # count is excluding the limit and so first decrease the right child and then add the left child
                right -= 1
                result += self.tree[right]
            right //= 2
        return result

    def update(self, index):
        index += self.offset + self.leaves
        self.tree[index] += 1
        while index > 1:
            # keep updating the parent node value too
            index //= 2
            self.tree[index] += 1
