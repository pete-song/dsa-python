class TreeNode:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, node, value):
    if not node:
      return TreeNode(value)
    if node.value == value:
      return node
    if node.value < value:
      node.right = self.insert(node.right, value)
    else:
      node.left = self.insert(node.left, value)
    return node

  def preorder(self, node):
    if node:
      print(node.value, end=' ')
      self.preorder(node.left)
      self.preorder(node.right)

  def inorder(self, node):
    if node:
      self.preorder(node.left)
      print(node.value, end=' ')
      self.preorder(node.right)

  def postorder(self, node):
    if node:
      self.preorder(node.left)
      self.preorder(node.right)
      print(node.value, end=' ')
