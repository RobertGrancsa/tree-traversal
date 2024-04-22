from node import Node


## @brief  Tree class for binary tree
class Tree:

    ## @brief  Constructor for Tree class
    def __init__(self):
        self.root = None

    ## @brief  Method for get root of the tree
    def getRoot(self):
        return self.root

    ## @brief  Method for add data to the tree
    def add(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    ## @brief Method for add data to the tree
    #
    #
    # @param		data	data to add
    #
    # @return
    # @return		            None
    #
    #
    # @protected
    def _add(self, data, node):
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    ## @brief Method for find data in the tree
    #
    #
    # @param		data	data to find
    #
    # @return
    # @return		Node	node with data
    #
    def find(self, data):
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
        self.root = None

    def printTree(self):
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        if node is not None:
            print(str(node.data) + ' ')
            self._printPreorderTree(node.left)
            self._printPreorderTree(node.right)

    def _printPostorderTree(self, node):
        if node is not None:
            self._printPostorderTree(node.left)
            self._printPostorderTree(node.right)
            print(str(node.data) + ' ')
