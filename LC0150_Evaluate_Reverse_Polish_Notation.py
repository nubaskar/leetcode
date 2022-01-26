"""
- Build NRL tree Loop:
- evaluate(Node) is a recursive function:
  + If Node is a NUMBER, return it is
  + evaluate(Right_Node)
  + evaluate(Left_Node)
  + If Node is +, return sum(Right_Node.value, Left_Node.value)
  + If Node is -, return subtract(Right_Node.value, Left_Node.value)
  + If Node is *, return multiply(Right_Node.value, Left_Node.value)
  + If Node is /, return 0
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.binary_tree = None
        self.stack = []

    def build_tree(self, tokens):
        operators = ['+', '-', '*', '/']

        for token in tokens[-1::-1]:
            node = Node(token)

            if not self.binary_tree:
                self.binary_tree = node # root node
                current_node = node
                continue

            if not current_node.right:
                current_node.right = node
            elif not current_node.left:
                current_node.left = node

            if token in operators:
                self.stack.append(current_node)
                current_node = node

            while current_node.right and current_node.left and current_node != self.binary_tree:
                current_node = self.stack.pop()

    def compute(self, current_node, right_node, left_node):
        if right_node == None and left_node == None:
            return current_node.val
        
        right_val = int(self.compute(right_node, right_node.right, right_node.left))
        left_val = int(self.compute(left_node, left_node.right, left_node.left))

        if current_node.val == "+":
            return left_val + right_val
        elif current_node.val == "-":
            return left_val - right_val
        elif current_node.val == "*":
            return left_val * right_val
        elif current_node.val == "/":
            return int(left_val / right_val)

    def evalRPN(self, tokens):
        self.build_tree(tokens)
        return self.compute(self.binary_tree, self.binary_tree.right, self.binary_tree.left)

if __name__ == '__main__':
    tokens = ["2","1","+","3","*"]
    result = Solution().evalRPN(tokens)
    print(result)

    tokens = ["4","13","5","/","+"]
    result = Solution().evalRPN(tokens)
    print(result)

    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    result = Solution().evalRPN(tokens)
    print(result)

    tokens = ["4","-2","/","2","-3","-","-"]
    result = Solution().evalRPN(tokens)
    print(result)
