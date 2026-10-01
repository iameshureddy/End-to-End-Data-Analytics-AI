from tools.calculator_tool import calculate

result = calculate.invoke(
    {
        "expression": "(25 + 15) * 2 / 4"
    }
)

print(result)