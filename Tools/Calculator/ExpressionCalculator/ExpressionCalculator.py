import ast
import math
import operator
from Global import Global


class ExpressionCalculator:
    BIN_OPS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
    }

    UNARY_OPS = {
        ast.UAdd: operator.pos,
        ast.USub: operator.neg,
    }

    FUNCTIONS = {
        "sqrt": math.sqrt,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "log": math.log,
        "abs": abs,
        "round": round,
    }

    CONSTANTS = {
        "pi": math.pi,
        "e": math.e,
    }

    def Start(self):
        while True:
            try:
                print("Expression Calculator".center(Global.HeaderFormatConstant, "="))
                print('Type "exit" to get back to the main menu')
                expression = input("Enter Expression: ").strip()

                if expression.lower() == "exit":
                    return

                if not expression:
                    continue

                result = self.Calculate(expression)
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                print(f"{"Result":<{Global.TextFormatConstant}}: {result}")

            except Exception as e:
                print(f"{"Error":<{Global.TextFormatConstant}}: {e}")

    def Calculate(self, userInput: str):
        parsed = ast.parse(userInput.strip(), mode="eval")
        return self._eval_node(parsed.body)

    def _eval_node(self, node):
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError(f"Unsupported constant type: {type(node.value).__name__}")

        if isinstance(node, ast.BinOp):
            op_type = type(node.op)
            if op_type not in self.BIN_OPS:
                raise ValueError(f"Unsupported binary operator: {op_type.__name__}")
            left = self._eval_node(node.left)
            right = self._eval_node(node.right)

            if op_type is ast.Pow:
                if right > 1000 or (abs(left) > 10 and right > 300):
                    raise ValueError("Exponent too large to evaluate safely")

            return self.BIN_OPS[op_type](left, right)

        if isinstance(node, ast.UnaryOp):
            op_type = type(node.op)
            if op_type not in self.UNARY_OPS:
                raise ValueError(f"Unsupported unary operator: {op_type.__name__}")
            return self.UNARY_OPS[op_type](self._eval_node(node.operand))

        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name) or node.func.id not in self.FUNCTIONS:
                func_name = getattr(node.func, "id", "Unknown")
                raise ValueError(f"Unsupported function: '{func_name}'")
            args = [self._eval_node(arg) for arg in node.args]
            return self.FUNCTIONS[node.func.id](*args)

        if isinstance(node, ast.Name):
            if node.id in self.CONSTANTS:
                return self.CONSTANTS[node.id]
            raise ValueError(f"Unknown symbol: '{node.id}'")

        raise ValueError(f"Unsupported expression syntax: {type(node).__name__}")
