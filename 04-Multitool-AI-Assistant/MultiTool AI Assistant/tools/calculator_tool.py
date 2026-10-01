"""
calculator_tool.py
------------------
LangChain tool to evaluate basic arithmetic expressions safely.
"""

import ast
import operator

from langchain_core.tools import tool

from utils.logger import logger


_ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
}


def _evaluate(node):
    if isinstance(node, ast.Constant):
        return node.value

    if isinstance(node, ast.Num):  # Compatibility
        return node.n

    if isinstance(node, ast.BinOp):
        left = _evaluate(node.left)
        right = _evaluate(node.right)
        return _ALLOWED_OPERATORS[type(node.op)](left, right)

    if isinstance(node, ast.UnaryOp):
        operand = _evaluate(node.operand)
        return _ALLOWED_OPERATORS[type(node.op)](operand)

    raise TypeError("Unsupported expression.")


@tool
def calculate(expression: str) -> str:
    """
    Evaluate a basic arithmetic expression.

    Example:
    calculate("25 * (5 + 3)")
    """

    try:
        logger.info(f"Calculator tool called: {expression}")

        tree = ast.parse(expression, mode="eval")

        result = _evaluate(tree.body)

        logger.info("Calculator tool executed successfully.")

        return str(result)

    except Exception as e:
        logger.error(f"Calculator tool error: {e}")
        return f"Error: {e}"