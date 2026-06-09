class TreeNode:
    def __init__(self,v,left=None,right=None):
        self.value = v
        self.left = left
        self.right = right


# Root → Left → Right
def preorder(node):
    if node is not None:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)

# Left → Root → Right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)

# Left → Right → Root
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")


root = TreeNode("A")
root.left = TreeNode("B")
root.left.left= TreeNode("G")
root.right = TreeNode("C")
root.right.right =TreeNode("E")

print(f"Root → Left → Right :")
print(preorder(root))

print(f"Left → Root → Right :")
print(inorder(root))

print(f"Left → Right → Root :")
print(postorder(root))