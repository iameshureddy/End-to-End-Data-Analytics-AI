from tools.currency_tool import get_exchange_rate

result = get_exchange_rate.invoke(
    {
        "base": "USD",
        "target": "INR",
    }
)

print(result)