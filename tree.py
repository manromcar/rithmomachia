class NonBinTree:

    def __init__(self, val):
        self.val = val
        self.nodes = []

    def add_node(self, val):
        self.nodes.append(NonBinTree(val))
    def max(self):
        res=self.nodes[0]
        val=self.nodes[0].val
        for node in self.nodes:
            if node.val > val:
                res= node
                val= node.val
        return res


a = NonBinTree(0)
a.add_node(1)
a.add_node(3)
a.add_node(4)
print(a.max())
for x in a.nodes:
    print(x)


