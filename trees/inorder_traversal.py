# Structure of a Binary Tree Node
class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

# Function to print preorder traversal
def inorder(node):
    if node is None:
        return

    # Recur on left subtree
    inorder(node.left)
    
    # Deal with the node
    print(node.data, end=' ')

    # Recur on right subtree
    inorder(node.right)

def test():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    
    inorder(root)

if __name__ == '__main__':
    test()

#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

# 4 2 5 1 3 6