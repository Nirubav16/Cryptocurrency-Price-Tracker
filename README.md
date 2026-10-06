# Cryptocurrency Price Tracker

## 📌 Project Description

The Cryptocurrency Price Tracker is a Python-based application designed
to collect and monitor cryptocurrency market information.

The project uses Selenium WebDriver to automate a web browser and
collect cryptocurrency information such as:

- Cryptocurrency name
- Current price
- 24-hour price change
- Market capitalization
- Rank
- Timestamp

The collected information is stored in CSV format for further analysis
and historical tracking.

---

## 🎯 Project Objective

The main objective of this project is to develop an automated
cryptocurrency price monitoring system.

The system can:

1. Collect cryptocurrency market data.
2. Track the top 10 cryptocurrencies.
3. Store cryptocurrency prices and market information.
4. Record the time at which the data was collected.
5. Maintain historical cryptocurrency data.
6. Filter cryptocurrency information.
7. Identify top gainers.
8. Provide data that can later be used for charts and dashboards.

---

## ✨ Features

### 1. Real-Time Price Tracking

The application collects the latest available cryptocurrency
market information.

### 2. Top 10 Cryptocurrency Tracking

The system focuses on the top 10 cryptocurrencies based on
market ranking/market capitalization.

### 3. Cryptocurrency Information

The following information is collected:

- Rank
- Cryptocurrency Name
- Symbol
- Current Price
- 24-Hour Change
- Market Capitalization
- Timestamp

### 4. CSV Data Storage

The collected data is stored in:

```text
data/crypto_data.csv
```

### 5. Historical Data Logging

Each data collection includes a timestamp.

Previous records are preserved so that cryptocurrency price changes
can be analyzed over time.

### 6. Filtering

The project can be extended to filter cryptocurrencies based on:

- Price
- 24-hour percentage change
- Market capitalization

### 7. Top Gainers

The project can identify cryptocurrencies with the highest
24-hour percentage increase.

### 8. Headless Browser Support

Selenium can run Chrome in headless mode without opening a visible
browser window.

---

## 🛠️ Technologies Used

The project is developed using:

- Python
- Selenium
- Pandas
- WebDriver Manager
- Google Chrome
- CSV

---

## 📁 Project Structure

```text
Cryptocurrency-Price-Tracker/
│
├── venv/
│
├── data/
│   └── crypto_data.csv
│
├── main.py
├── scraper.py
├── filters.py
├── config.py
├── requirements.txt
└── README.md
```

---

## 📄 File Description

### `main.py`

The main program file.

It:

- Starts the application
- Calls the scraper
- Processes the collected data
- Adds timestamps
- Saves data into CSV

---

### `scraper.py`

Contains the data collection logic.

Selenium WebDriver is used to automate the browser and collect
cryptocurrency information.

---

### `filters.py`

Contains functions for filtering and sorting cryptocurrency data.

Examples:

- Filter by price
- Find top gainers
- Sort cryptocurrency data

---

### `config.py`

Contains project configuration values such as:

```python
TOP_COINS = 10
```

and the CSV file location.

---

### `requirements.txt`

Contains the Python packages required to run the project.

---

### `data/crypto_data.csv`

Stores the collected cryptocurrency data and historical records.

---

# ⚙️ Installation

## Step 1: Install Python

Install Python 3.x on your computer.

Check the installation:

```bash
python --version
```

---

## Step 2: Clone or Download the Project

Open the project folder in Visual Studio Code.

---

## Step 3: Create a Virtual Environment

Open the VS Code terminal:

```bash
python -m venv venv
```

---

## Step 4: Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

After activation, the terminal should show:

```text
(venv)
```

---

## Step 5: Install Dependencies

Run:

```bash
pip install -r requirements.txt
```

Or install the packages manually:

```bash
pip install selenium pandas webdriver-manager
```

---

# ▶️ Running the Project

Make sure the virtual environment is activated.

Run:

```bash
python main.py
```

The application will collect cryptocurrency information and
store it in the CSV file.

---

# 📊 Output

The output contains information similar to:

| Rank | Coin | Symbol | Price | 24h Change | Market Cap | Timestamp |
|------|------|--------|-------|------------|------------|-----------|
| 1 | Bitcoin | BTC | ... | ... | ... | ... |
| 2 | Ethereum | ETH | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... | ... | ... |

The actual cryptocurrency prices change continuously according
to the market.

---

# 📂 CSV Storage

The collected information is stored in:

```text
data/crypto_data.csv
```

Example:

```text
Rank,Coin,Symbol,Price,24h Change,Market Cap,Timestamp
1,Bitcoin,BTC,...,...,...,2026-10-06 15:00:00
2,Ethereum,ETH,...,...,...,2026-10-06 15:00:00
```

When the tracker runs again, new timestamped records can be
added to the historical dataset.

---

# 🔎 Filtering

The project can filter cryptocurrency data based on price
or 24-hour percentage change.

For example:

```python
top_gainers(df)
```

can be used to identify cryptocurrencies with higher
24-hour percentage changes.

---

# 🌐 Selenium

Selenium WebDriver is used for browser automation.

The general workflow is:

```text
Start Python
     ↓
Start Selenium WebDriver
     ↓
Open Cryptocurrency Website
     ↓
Load Dynamic Content
     ↓
Collect Top 10 Cryptocurrencies
     ↓
Process Data
     ↓
Add Timestamp
     ↓
Save to CSV
```

---

# 🖥️ Headless Mode

The application can also run Chrome without displaying
the browser window.

In `config.py`:

```python
HEADLESS = True
```

To show the browser:

```python
HEADLESS = False
```

---

# 📈 Historical Analysis

Because the collected data contains timestamps, multiple
records can be stored and analyzed over time.

Example:

```text
10:00 AM → Bitcoin → Price A
10:05 AM → Bitcoin → Price B
10:10 AM → Bitcoin → Price C
```

This historical data can later be used to create:

- Price charts
- Trend analysis
- Market reports
- Cryptocurrency dashboards

---

# 🚀 Future Enhancements

The project can be extended with:

- Interactive dashboard
- Price charts
- Portfolio tracking
- Price alerts
- Email notifications
- Database storage
- Advanced filtering
- Historical trend visualization
- Automated scheduled scraping
- Web-based dashboard

---

# 🎓 Project Outcomes

The project demonstrates practical knowledge of:

- Python programming
- Web automation
- Selenium WebDriver
- Dynamic web-page handling
- Data extraction
- Pandas
- CSV file handling
- Historical data logging
- Data filtering
- Basic cryptocurrency market analysis

---

# ⚠️ Note

Cryptocurrency prices are highly dynamic and can change frequently.

The application is intended for educational and software-development
purposes and should not be considered financial advice.

---

# 👨‍💻 Project

**Project Name:** Cryptocurrency Price Tracker

**Language:** Python

**Automation Tool:** Selenium WebDriver

**Data Processing:** Pandas

**Storage:** CSV

**Browser:** Google Chrome# Cryptocurrency-Price-Tracker
