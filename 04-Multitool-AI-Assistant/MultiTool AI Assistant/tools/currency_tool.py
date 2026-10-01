"""
currency_tool.py
----------------
LangChain tool to fetch live currency exchange rates using Frankfurter API.
"""

import requests
from langchain_core.tools import tool

from config import CURRENCY_API_URL
from utils.logger import logger


@tool
def get_exchange_rate(base: str, target: str) -> str:
    """
    Get the latest exchange rate between two currencies.

    Args:
        base: Base currency code (e.g. USD)
        target: Target currency code (e.g. INR)

    Returns:
        Exchange rate as a formatted string.
    """

    try:
        base = base.upper()
        target = target.upper()

        logger.info(
            f"Currency tool called ({base} -> {target})"
        )

        response = requests.get(
            CURRENCY_API_URL,
            params={
                "from": base,
                "to": target,
            },
            timeout=10,
        )

        response.raise_for_status()

        data = response.json()

        if "rates" not in data or target not in data["rates"]:
            return "Exchange rate not available."

        rate = data["rates"][target]

        logger.info("Currency tool executed successfully.")

        return f"1 {base} = {rate} {target}"

    except Exception as e:
        logger.error(f"Currency tool error: {e}")
        return f"Error fetching exchange rate: {e}"