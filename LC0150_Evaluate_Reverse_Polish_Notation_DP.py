class ReversePolishNotation:
    def __init__(self):
        self.stack = []

    def evaluate_rpn_with_stack(self, tokens):
        operators = [ '+', '-', '*', '/']

        for token in tokens:
            if token not in operators: # token is a Number
                self.stack.append(int(token))
            else:
                # Operator, right_operand, left_operand
                result = self.compute(token, self.stack.pop(), self.stack.pop())
                self.stack.append(result)

        return self.stack.pop()

    def compute(self, operator, right_operand, left_operand):
        if operator == '+': # Addition
            return left_operand + right_operand
        elif operator == '-': # Subtraction
            return left_operand - right_operand
        elif operator == '*': # Multiplication
            return left_operand * right_operand
        elif operator == '/': # Division
            return int(left_operand / right_operand)

if __name__ == "__main__":
    tokens_1 = ["2","1","+","3","*"]
    print(ReversePolishNotation().evaluate_rpn_with_stack(tokens_1))

    tokens_2 = ["4", "13", "5", "/", "+"]
    print(ReversePolishNotation().evaluate_rpn_with_stack(tokens_2))

    tokens_3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(ReversePolishNotation().evaluate_rpn_with_stack(tokens_3))