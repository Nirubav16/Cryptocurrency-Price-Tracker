import csv
import os
import time
import logging
from datetime import datetime

import requests


# ============================================================
# CONFIGURATION
# ============================================================

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

CSV_FILE = "crypto_data.csv"

TOP_COINS = 10

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "tracker.log")


# ============================================================
# LOGGING
# ============================================================

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


# ============================================================
# API REQUEST
# ============================================================

def get_crypto_data():
    """
    Fetch top cryptocurrency data from CoinGecko.
    Returns a list of dictionaries.
    """

    print("\n==========================================")
    print("   CRYPTOCURRENCY PRICE TRACKER")
    print("==========================================")
    print("\nConnecting to cryptocurrency API...")

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": TOP_COINS,
        "page": 1,
        "sparkline": "false",
        "price_change_percentage": "24h"
    }

    headers = {
        "accept": "application/json",
        "user-agent": "CryptocurrencyPriceTracker/1.0"
    }

    for attempt in range(1, 4):

        try:

            print(f"Attempt {attempt}/3...")

            response = requests.get(
                API_URL,
                params=params,
                headers=headers,
                timeout=30
            )

            response.raise_for_status()

            data = response.json()

            if not data:
                raise ValueError("API returned empty data.")

            print("API connection successful!")
            logger.info("Cryptocurrency API connected successfully.")

            return data

        except requests.exceptions.RequestException as error:

            logger.warning(
                f"API attempt {attempt} failed: {error}"
            )

            print(f"Connection failed: {error}")

            if attempt < 3:
                print("Retrying in 5 seconds...")
                time.sleep(5)

            else:
                print("\nERROR: Unable to connect to cryptocurrency API.")
                logger.error("All API connection attempts failed.")

        except Exception as error:

            logger.error(
                f"Unexpected API error: {error}"
            )

            print(f"Unexpected error: {error}")

            break

    return []


# ============================================================
# VALIDATE AND FORMAT DATA
# ============================================================

def format_crypto_data(api_data):

    crypto_data = []

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    print("\nProcessing cryptocurrency data...\n")

    for coin in api_data:

        try:

            name = str(
                coin.get("name", "")
            ).strip()

            symbol = str(
                coin.get("symbol", "")
            ).upper().strip()

            price = coin.get("current_price")

            change_24h = coin.get(
                "price_change_percentage_24h"
            )

            market_cap = coin.get(
                "market_cap"
            )

            # --------------------------------------------
            # VALIDATION
            # --------------------------------------------

            if not name:
                logger.warning(
                    "Skipped coin: empty name"
                )
                continue

            if not symbol:
                logger.warning(
                    f"Skipped {name}: empty symbol"
                )
                continue

            if price is None:
                logger.warning(
                    f"Skipped {name}: missing price"
                )
                continue

            if price <= 0:
                logger.warning(
                    f"Skipped {name}: invalid price"
                )
                continue

            if change_24h is None:
                change_24h = 0.0

            if market_cap is None:
                market_cap_text = ""
            else:
                market_cap_text = format_market_cap(
                    market_cap
                )

            # --------------------------------------------
            # CREATE RECORD
            # --------------------------------------------

            record = {
                "timestamp": timestamp,
                "name": name,
                "symbol": symbol,
                "price_usd": round(float(price), 8),
                "change_24h_pct": round(
                    float(change_24h), 2
                ),
                "market_cap_usd": market_cap_text
            }

            crypto_data.append(record)

        except Exception as error:

            logger.warning(
                f"Error processing coin: {error}"
            )

            continue

        if len(crypto_data) >= TOP_COINS:
            break

    return crypto_data


# ============================================================
# MARKET CAP FORMAT
# ============================================================

def format_market_cap(value):

    try:

        value = float(value)

        if value >= 1_000_000_000_000:
            return f"${value / 1_000_000_000_000:.2f}T"

        elif value >= 1_000_000_000:
            return f"${value / 1_000_000_000:.2f}B"

        elif value >= 1_000_000:
            return f"${value / 1_000_000:.2f}M"

        elif value >= 1_000:
            return f"${value / 1_000:.2f}K"

        else:
            return f"${value:.2f}"

    except Exception:

        return ""


# ============================================================
# SAVE DATA TO CSV
# ============================================================

def save_to_csv(crypto_data):

    if not crypto_data:

        print("\nNo cryptocurrency data to save.")
        logger.warning("No cryptocurrency data available.")

        return False

    fieldnames = [
        "timestamp",
        "name",
        "symbol",
        "price_usd",
        "change_24h_pct",
        "market_cap_usd"
    ]

    file_exists = os.path.exists(CSV_FILE)

    try:

        with open(
            CSV_FILE,
            "a",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            # Write header only for a new CSV
            if not file_exists:
                writer.writeheader()

            writer.writerows(crypto_data)

        print("\n==========================================")
        print("          DATA SAVED SUCCESSFULLY")
        print("==========================================")

        print(
            f"\n{len(crypto_data)} cryptocurrency records "
            f"saved to {CSV_FILE}"
        )

        logger.info(
            f"{len(crypto_data)} cryptocurrency records saved."
        )

        return True

    except PermissionError:

        print("\nERROR: crypto_data.csv is open.")

        print(
            "Please close crypto_data.csv in Excel "
            "and run the program again."
        )

        logger.error(
            "Permission denied while writing CSV."
        )

        return False

    except Exception as error:

        print(
            f"\nERROR while saving CSV: {error}"
        )

        logger.error(
            f"CSV save error: {error}"
        )

        return False


# ============================================================
# DISPLAY DATA
# ============================================================

def display_data(crypto_data):

    print("\n")
    print("=" * 90)
    print("TOP 10 CRYPTOCURRENCIES")
    print("=" * 90)

    for index, coin in enumerate(
        crypto_data,
        start=1
    ):

        print(
            f"{index}. "
            f"{coin['name']} "
            f"({coin['symbol']})"
        )

        print(
            f"   Price       : ${coin['price_usd']}"
        )

        print(
            f"   24h Change  : "
            f"{coin['change_24h_pct']}%"
        )

        print(
            f"   Market Cap  : "
            f"{coin['market_cap_usd']}"
        )

        print("-" * 90)


# ============================================================
# MAIN SCRAPER FUNCTION
# ============================================================

def scrape_crypto_data():

    print("\nStarting cryptocurrency price tracker...")

    # Get data from API
    api_data = get_crypto_data()

    if not api_data:

        print("\nFAILED: No data received.")
        return []

    # Format and validate
    crypto_data = format_crypto_data(
        api_data
    )

    if len(crypto_data) < TOP_COINS:

        print(
            f"\nWARNING: Only {len(crypto_data)} "
            f"valid records collected."
        )

    # Display
    display_data(crypto_data)

    # Save
    saved = save_to_csv(
        crypto_data
    )

    if saved:

        print("\nSUCCESS!")
        print(
            "Cryptocurrency data has been "
            "stored in crypto_data.csv"
        )

    return crypto_data


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":

    try:

        scrape_crypto_data()

    except KeyboardInterrupt:

        print("\n\nProgram stopped by user.")

    except Exception as error:

        print(
            f"\nPROGRAM ERROR: {error}"
        )

        logger.exception(
            "Unexpected program error."
        )