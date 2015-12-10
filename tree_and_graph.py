# @tigreen


class TreeNode():
    """A class representing a tree node."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree():
    """
    A class representing a Binary Tree (BT). Max 2 children.
    Has a pointer to its parent as well.
    """
    def __init__(self, root, size=0):
        self.root = root
        self.size = size

    def inorder(self, root, lst):
        if root == None:
            return
        # left -> root -> right
        self.inorder(root.left, lst)
        lst.append(root.data)
        self.inorder(root.right, lst)

    def preorder(self, root):
        if root == None:
            return
        # root -> left -> right
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self, root):
        if root == None:
            return
        # left -> right -> current node
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)

    def find_node_in_bst(self, root, data):
        """
        Find the node that has the given data in BST.
        """
        if root == None:
            return None

        if root.data == data:
            return root.data
        if data < root.data:
            return self.find_node_in_bst(root.left, data)
        elif data > root.data:
            return self.find_node_in_bst(root.right, data)

    def delete_node_bst(self, root, dvalue):
        """
        Delete a node from a binary search tree.
        Case 1: The removed node is a leaf node
        Case 2: The removed node has only one subtree
        Case 3: The removed node has its two subtrees.
        """
        if root == None:
            return False

        if root.data == dvalue:
            # Case 1. Root is a leaf node
            if root.left is None and root.right is None:
                root = None
                return True

            # Case 2. Has only one substree
            if root.left is None or root.right is None:

                if root.left is not None:
                    temp_left = root.left
                    if temp_left.is_left_child():
                        root.parent.left = temp_left
                    if temp_left.is_right_child():
                        root.parent.right = temp_left

                if root.right != None:
                    temp_right = root.right
                    if temp_right.is_left_child():
                        root.parent.left = temp_right
                    if temp_right.is_right_child():
                        root.parent.right = temp_right
            # Case 3
            if root.left != None and root.right != None:
                # Some code here
                pass

            self.delete_node_bst(root.left, dvalue)
            self.delete_node_bst(root.right, dvalue)

        else:
            return False

    # A helper func for deleteNode.
    # In a BST the max node is the right most node.
    def findMaxNode(self, root):
        if root == None:
            return None

        tempRoot = root
        while tempRoot.right != None:
            tempRoot = tempRoot.right

        return tempRoot.data

    def insert_node_BST(self, root, data):
        """
        Creates a new node with the given data and inserts it to the tree.
        """

        if root is None:
            self.size += 1
            root = TreeNode(data, None, None)

        elif data <= root.data:
            root.left = self.insert_node_BST(root.left, data)
        else:
            root.right = self.insert_node_BST(root.right, data)

        return root

    def isBalancedTree(self, root):
        """
        Balanced if max_depth - min_depth <= 1
        """
        min_depth = self.min_depth(root)
        max_depth = self.max_depth(root)

        if max_depth - min_depth <= 1:
            return True
        else:
            return False

    """
    Option 1.
    We can do inOrder traversal and see
    if the array is sorted. If it is then
    the tree is a BST.
    """

    def is_bst(self, root):
        if root == None:
            return True
        lst = []
        self.inorder(root, lst)
        if sorted(lst) == lst:
            return True
        else:
            return False

    """
    Option 2.
    Recursive approach.
    Condition: Every left node is less than or equal its parent
    and every right node it greater than the parent.
    Any node in the left subtree must be less than any node in the
    right subtree.
    """

    def is_valid_bst(self, root):
        return self.is_bst_util(root, -1000, 1000)

    def is_bst_util(self, root, mn, mx):
        if root is None:
            return True

        return (root.data > mn and root.data <= mx and
                self.is_bst_util(root.left, mn, root.data)
                and self.is_bst_util(root.right, root.data, mx))

    def max_depth(self, root):
        if root == None:
            return -1

        left_max = 1 + self.max_depth(root.left)
        right_max = 1 + self.max_depth(root.right)

        return max(left_max, right_max)

    # the miniumum depth of the tree.
    def min_depth(self, root):
        if root == None:
            return -1
        left_min = 1 + self.min_depth(root.left)
        right_min = 1 + self.min_depth(root.right)

        return min(left_min, right_min)

    #Depth first search on a graph. 
    def dfs(self, root):
        if root == None:
            return root

        print(root.data)
        root.visited = True
        for each n node that is root.adjacent:
            if n.is_visited == False:
                dfs(n)

    def creat_min_bt(self, arr):
        """
        Given a sorted(increasing order) array, write an algo to
        create a binary tree with min height
        """
        if arr == None:
            return None

        middle = len(arr//2)

        root = TreeNode(arr[middle])
        root.left = self.creat_min_bt(arr[:middle])
        root.right = self.creat_min_bt(arr[middle+1:])

        return root
