import os
from datetime import datetime

import pandas as pd

from scraper import scrape_crypto_data
from config import CSV_FILE
from filters import top_gainers


# ============================================================
# SAVE CRYPTOCURRENCY DATA
# ============================================================

def save_data(data):

    if not data:
        print("\nNo cryptocurrency data found.")
        return None

    # Create folder only when a folder is specified
    folder = os.path.dirname(CSV_FILE)

    if folder:
        os.makedirs(folder, exist_ok=True)

    # Convert scraped data to DataFrame
    df = pd.DataFrame(data)

    # Add timestamp
    df["Timestamp"] = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    # Check whether CSV already exists
    file_exists = os.path.exists(CSV_FILE)

    # Save data
    df.to_csv(
        CSV_FILE,
        mode="a",
        header=not file_exists,
        index=False
    )

    print("\n" + "=" * 70)
    print("DATA SAVED SUCCESSFULLY")
    print("=" * 70)

    print(
        len(df),
        "cryptocurrency records saved to",
        CSV_FILE
    )

    return df


# ============================================================
# DISPLAY CRYPTOCURRENCY DATA
# ============================================================

def display_data(df):

    print("\n" + "=" * 70)
    print("CURRENT CRYPTOCURRENCY DATA")
    print("=" * 70)

    print(df.to_string(index=False))

    # ========================================================
    # TOP GAINERS
    # ========================================================

    print("\n")
    print("=" * 70)
    print("TOP GAINERS")
    print("=" * 70)

    try:

        # Convert DataFrame into list of dictionaries
        records = df.to_dict("records")

        # Get top gainers
        gainers = top_gainers(records, count=5)

        if not gainers:
            print("No top gainers found.")
            return

        # Convert list back to DataFrame
        gainers_df = pd.DataFrame(gainers)

        # ----------------------------------------------------
        # Find correct column names from your scraper
        # ----------------------------------------------------

        name_column = None
        price_column = None
        change_column = None

        # Name
        for column in [
            "Coin",
            "coin_name",
            "name",
            "Name"
        ]:
            if column in gainers_df.columns:
                name_column = column
                break

        # Price
        for column in [
            "Price",
            "price",
            "price_usd",
            "Price USD"
        ]:
            if column in gainers_df.columns:
                price_column = column
                break

        # 24h Change
        for column in [
            "24h Change",
            "change_24h",
            "change_24h_pct",
            "price_change_percentage_24h",
            "24h_change"
        ]:
            if column in gainers_df.columns:
                change_column = column
                break

        # ----------------------------------------------------
        # Display selected columns
        # ----------------------------------------------------

        display_df = pd.DataFrame()

        if name_column:
            display_df["Coin"] = gainers_df[name_column]

        if price_column:
            display_df["Price"] = gainers_df[price_column]

        if change_column:
            display_df["24h Change"] = gainers_df[change_column]

        if display_df.empty:
            print("Unable to find cryptocurrency columns.")
        else:
            print(
                display_df.to_string(index=False)
            )

    except Exception as error:

        print(
            "\nFiltering error:",
            error
        )


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("\n")
    print("=" * 70)
    print("       CRYPTOCURRENCY PRICE TRACKER")
    print("=" * 70)

    print("\nCollecting cryptocurrency data...")

    # Get cryptocurrency data
    data = scrape_crypto_data()

    # Save data
    df = save_data(data)

    # Display data and top gainers
    if df is not None:

        display_data(df)

    print("\n")
    print("=" * 70)
    print("PROGRAM COMPLETED SUCCESSFULLY")
    print("=" * 70)


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()