# ============================================================
# CRYPTOCURRENCY PRICE TRACKER - FILTERS
# ============================================================

def _get_change(coin):
    """
    Safely get 24h percentage change from a cryptocurrency record.
    Supports both dictionary data and pandas DataFrame rows.
    """

    if hasattr(coin, "to_dict"):
        coin = coin.to_dict()

    if not isinstance(coin, dict):
        return 0.0

    value = coin.get("change_24h")

    if value is None:
        value = coin.get("change_24h_pct")

    if value is None:
        value = coin.get("price_change_percentage_24h")

    if value is None:
        value = coin.get("24h_change")

    try:
        if isinstance(value, str):
            value = value.replace("%", "").replace(",", "").strip()

        return float(value)

    except (ValueError, TypeError):
        return 0.0


def _get_name(coin):
    """Safely get cryptocurrency name."""

    if hasattr(coin, "to_dict"):
        coin = coin.to_dict()

    if not isinstance(coin, dict):
        return "Unknown"

    return str(
        coin.get("name")
        or coin.get("coin_name")
        or coin.get("Name")
        or "Unknown"
    )


def top_gainers(data, count=5):
    """
    Return cryptocurrencies with the highest 24h percentage increase.
    """

    if data is None:
        return []

    # Convert DataFrame to list of dictionaries if necessary
    if hasattr(data, "to_dict"):
        try:
            data = data.to_dict("records")
        except TypeError:
            data = data.to_dict()

    if not isinstance(data, list):
        return []

    # Sort safely by 24h change
    sorted_data = sorted(
        data,
        key=_get_change,
        reverse=True
    )

    return sorted_data[:count]


def top_losers(data, count=5):
    """
    Return cryptocurrencies with the lowest 24h percentage change.
    """

    if data is None:
        return []

    # Convert DataFrame to list of dictionaries if necessary
    if hasattr(data, "to_dict"):
        try:
            data = data.to_dict("records")
        except TypeError:
            data = data.to_dict()

    if not isinstance(data, list):
        return []

    # Sort safely from lowest to highest
    sorted_data = sorted(
        data,
        key=_get_change
    )

    return sorted_data[:count]


def filter_by_change(data, minimum_change=0.0):
    """
    Return cryptocurrencies whose 24h change is
    greater than or equal to minimum_change.
    """

    if data is None:
        return []

    if hasattr(data, "to_dict"):
        try:
            data = data.to_dict("records")
        except TypeError:
            data = data.to_dict()

    if not isinstance(data, list):
        return []

    result = []

    for coin in data:
        if _get_change(coin) >= minimum_change:
            result.append(coin)

    return result


def print_coin(coin, position=None):
    """Print one cryptocurrency in a clean format."""

    name = _get_name(coin)
    change = _get_change(coin)

    symbol = ""

    if isinstance(coin, dict):
        symbol = coin.get("symbol", "")

    price = ""

    if isinstance(coin, dict):
        price = coin.get("price")

        if price is None:
            price = coin.get("price_usd")

    market_cap = ""

    if isinstance(coin, dict):
        market_cap = coin.get("market_cap")

        if market_cap is None:
            market_cap = coin.get("market_cap_usd")

    if position is not None:
        print(f"{position}. {name} ({symbol})")
    else:
        print(f"{name} ({symbol})")

    print(f"   Price       : ${price}")
    print(f"   24h Change  : {change:.2f}%")
    print(f"   Market Cap  : ${market_cap}")
    print("-" * 60)


def display_top_gainers(data, count=5):
    """Display top gaining cryptocurrencies."""

    print("\n")
    print("=" * 60)
    print("TOP GAINERS")
    print("=" * 60)

    gainers = top_gainers(data, count)

    if not gainers:
        print("No gainers found.")
        return

    for i, coin in enumerate(gainers, start=1):
        print_coin(coin, i)


def display_top_losers(data, count=5):
    """Display top losing cryptocurrencies."""

    print("\n")
    print("=" * 60)
    print("TOP LOSERS")
    print("=" * 60)

    losers = top_losers(data, count)

    if not losers:
        print("No losers found.")
        return

    for i, coin in enumerate(losers, start=1):
        print_coin(coin, i)


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":

    print("Filters module loaded successfully.")