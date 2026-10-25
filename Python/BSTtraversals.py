class Node:
    def __init__(self,item):
        self.data=item
        self.left=None
        self.right=None
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)
def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data,end=" ")
def minvalue(node):
    while node.left!=None:
        node=node.left
    return node
def maxvalue(node):
    while node.right!=None:
        node=node.right
    return node
def insert(node,key):
    if node==None:
        return Node(key)
    if key<node.data:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
# def deleteNode(root,key):
#     if root==None:
#         return root
#     if key<root.data:
#         root.left=deleteNode(root.left,key)
#     elif key>root.data:
#         root.right=deleteNode(root.right,key)
#     else:
#         if root.left==None:
#             temp=root.right
#             root=None
#             return temp
#         elif root.right==None:
#             temp=root.left
#             root=None
#             return temp
#         temp=minvalue(root.right)
#         root.data=temp.data
#         root.right=deleteNode(root.right,temp.data)
#         return root
root=None
root =insert(root,8)
root=insert(root,3)
root=insert(root,1)
root=insert(root,6)
root=insert(root,7)
root=insert(root,10)
root=insert(root,14)
root=insert(root,4)
print("element in preorder")
preorder(root)
print()
print("element in inorder")
inorder(root)
print()
node=minvalue(root)
print("minimum value is",node.data)
node=maxvalue(root)
print("maximum value is",node.data)