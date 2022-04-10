class BinaryIndexedTree:
    def __init__(self, offset):
        """
        Binary-indexed-tree (BIT) for calculating prefix frequency
        :param offset:
        """
        self.offset = offset
        self.size = 2 * (offset + 1)  # total possible values plus one dummy for the root
        self.tree = [0 for _ in range(self.size)]

    def update(self, index):
        index += self.offset + 1  # index in BIT is one more than the original index
        while index < self.size:
            # iteratively increment child values so that child saves count of nums in [parent, child).
            self.tree[index] += 1
            # find the next child
            index += index & -index

    def query(self, index):
        # index in BIT is one more than the original index but here it is not incremented
        # because we want value smaller than the current
        index += self.offset
        count = 0
        # index 0 is dummy root node and so check only till 1.
        while index >= 1:
            count += self.tree[index]
            # find the parent and add the value
            index -= index & -index
        return count
