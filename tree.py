from collections import deque

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def inorder(self):
        if self.left:
            self.left.inorder()
        
        print(self.value)

        if self.right:
            self.right.inorder()

    def bfs(self):
        queue = deque()
        queue.append(self)

        while queue:
            node = queue.popleft()
            print(f"{node.value=}")

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

    def insert_node(self, value):
        new_node = BinarySearchTree(value)

        if value <= self.value and self.left:
            self.left.insert_node(value)
        elif value > self.value and self.right:
            self.right.insert_node(value)
        elif value <= self.value:
            self.left = new_node
        else:
            self.right = new_node

    def clear_node(self):
        self.value = None
        self.left = None
        self.right = None
    
    def find_second_root(self):
        if self.left:
            return self.left.find_second_root()
        else:
            return self.value
    
    def remove_node(self, value, parent):
        if value < self.value and self.left:
            self.left.remove_node(value, self)
        elif value < self.value:
            return False
        elif value > self.value and self.right:
            self.right.remove_node(value, self)
        elif value > self.value:
            return False
        else:
            if self.left is None and self.right is None and self == parent.left:
                parent.left = None
                self.clear_node()
            elif self.left is None and self.right is None and self == parent.right:
                parent.right = None
                self.clear_node()
            elif self.left and self.right is None and self == parent.left:
                parent.left = self.left
                self.clear_node()
            elif self.left and self.right is None and self == parent.right:
                parent.right = self.left
                self.clear_node()
            elif self.left is None and self.right and self == parent.left:
                parent.left = self.right
                self.clear_node()
            elif self.left is None and self.right and self == parent.right:
                parent.right = self.right
                self.clear_node()
            else:
                self.value = self.right.find_second_root()
                self.right.remove_node(self.value, self)


if __name__ == "__main__":
    root = BinarySearchTree(5)
    root.insert_node(3)
    root.insert_node(9)
    root.insert_node(7)
    root.insert_node(10)
    root.insert_node(4)
    root.insert_node(1)

    # root.inorder()

    root.bfs()

    root.remove_node(5, None)

    root.bfs()

