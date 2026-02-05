if __name__ == "__main__":
    strategy = TradingStrategy("AAPL", "2018-01-01", "2023-12-31")
    data = strategy.fetch_data()
    profit = strategy.apply_strategy(data)

    print("Trades:", strategy.trades)
    print("Final Profit/Loss:", round(profit, 2))
