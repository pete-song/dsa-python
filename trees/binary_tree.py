class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self):
    self.root = None

  # Preorder Traversal (Root-Left-Right)
  def preorder(self, node, result=None):
    if result is None:
      result = []
    if node:
      result.append(node.value)
      self.preorder(node.left, result)
      self.preorder(node.right, result)
    return result

  # Inorder Traversal (Left-Root-Right)
  def inorder(self, node, result=None):
    if result is None:
      result = []
    if node:
      self.inorder(node.left, result)
      result.append(node.value)
      self.inorder(node.right, result)
    return result

  # Postorder Traversal (Left-Right-Root)
  def postorder(self, node, result=None):
    if result is None:
      result = []
    if node:
      self.postorder(node.left, result)
      self.postorder(node.right, result)
      result.append(node.value)
    return result

  # Level Order Traversal (BFS)
  def level_order_traversal(self):
    if not self.root:
      return []
    queue = [self.root]
    result = []
    while queue:
      node = queue.pop(0)
      result.append(node.value)
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
    return result

  # Get height of the tree
  def height(self, node):
    if not node:
      return 0
    return 1 + (max(self.height(node.left), self.height(node.right)))

  # Count total nodes in the tree
  def count_nodes(self, node):
    if not node:
      return 0
    return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

  # Check if the tree is balanced
  def is_balanced(self, node):
    def check_height(node):
      if not node:
        return 0  # Height of an empty tree is 0

      left_height = check_height(node.left)
      if left_height == -1:
        return -1  # Left subtree is unbalanced

      right_height = check_height(node.right)
      if right_height == -1:
        return -1  # Right subtree is unbalanced

      if abs(left_height - right_height) > 1:
        return -1  # Current tree is unbalanced

      return max(left_height, right_height) + 1  # Return height of the current node

    return check_height(node) != -1  # If -1 is returned, the tree is unbalanced

  # Mirror the tree (Swap left and right subtrees)
  def mirror_tree(self, node):
    if node:
      node.left, node.right = node.right, node.left
      self.mirror_tree(node.left)
      self.mirror_tree(node.right)

  # Diameter of the tree (Longest path between two nodes)
  def diameter(self, node):
    if not node:
      return 0
    left_height = self.height(node.left)
    right_height = self.height(node.right)
    left_diameter = self.diameter(node.left)
    right_diameter = self.diameter(node.right)
    return max(left_height + right_height, max(left_diameter, right_diameter))

  # Check if two trees are identical
  def is_identical(self, root1, root2):
    if not root1 and not root2:
      return True
    if root1 and root2 and root1.value == root2.value:
      return self.is_identical(root1.left, root2.left) and self.is_identical(root1.right, root2.right)
    return False

  # Serialize the tree (convert to list representation)
  def serialize(self, node):
    if not node:
      return ['#']
    return [node.value] + self.serialize(node.left) + self.serialize(node.right)

  # Deserialize a list back to a tree
  def deserialize(self, data):
    def helper():
      value = next(data)
      if value == '#':
          return None
      node = TreeNode(value)
      node.left = helper()
      node.right = helper()
      return node
    return helper()

import unittest

class TestBinaryTree(unittest.TestCase):
  def setUp(self):
    self.tree = BinaryTree()
    self.tree.root = TreeNode(1)
    self.tree.root.left = TreeNode(2)
    self.tree.root.right = TreeNode(3)
    self.tree.root.left.left = TreeNode(4)
    self.tree.root.left.right = TreeNode(5)
    self.tree.root.right.left = TreeNode(6)
    self.tree.root.right.right = TreeNode(7)

  def test_preorder(self):
    result = []
    self.tree.preorder(self.tree.root, result)
    self.assertEqual(result, [1, 2, 4, 5, 3, 6, 7])

  def test_inorder(self):
    result = []
    self.tree.inorder(self.tree.root, result)
    self.assertEqual(result, [4, 2, 5, 1, 6, 3, 7])

  def test_postorder(self):
    result = []
    self.tree.postorder(self.tree.root, result)
    self.assertEqual(result, [4, 5, 2, 6, 7, 3, 1])

  def test_level_order_traversal(self):
    result = []
    self.tree.level_order_traversal()
    self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7])

  def test_height(self):
    self.assertEqual(self.tree.height(self.tree.root), 3)

  def test_count_nodes(self):
    self.assertEqual(self.tree.count_nodes(self.tree.root), 7)

  def test_is_balanced(self):
    self.assertTrue(self.tree.is_balanced(self.tree.root))

  def test_mirror_tree(self):
    self.tree.mirror_tree(self.tree.root)
    self.assertEqual(self.tree.root.left.value, 3)
    self.assertEqual(self.tree.root.right.value, 2)

  def test_diameter(self):
      self.assertEqual(self.tree.diameter(self.tree.root), 4)

  def test_is_identical(self):
    tree2 = BinaryTree()
    tree2.root = TreeNode(1)
    tree2.root.left = TreeNode(2)
    tree2.root.right = TreeNode(3)
    tree2.root.left.left = TreeNode(4)
    tree2.root.left.right = TreeNode(5)
    tree2.root.right.left = TreeNode(6)
    tree2.root.right.right = TreeNode(7)
    self.assertTrue(self.tree.is_identical(self.tree.root, tree2.root))

  def test_serialize_deserialize(self):
    serialized = self.tree.serialize(self.tree.root)
    deserialized_tree = self.tree.deserialize(iter(serialized))
    self.assertTrue(self.tree.is_identical(self.tree.root, deserialized_tree))

if __name__ == "__main__":
  unittest.main()
