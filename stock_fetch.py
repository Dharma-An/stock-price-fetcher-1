import yfinance as yf

# Your stock list
tickers = ["DELHIVERY.NS", "BPCL.NS", "SAIL.NS"]

for t in tickers:
    stock = yf.Ticker(t)
    data = stock.history(period="1d", interval="1m")
    price = data["Close"].iloc[-1]
    print(f"{t} = ₹{price:.2f}")
