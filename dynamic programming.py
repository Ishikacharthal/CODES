def rod_cutting(prices, n):
    dp = [0] * (n + 1)
    first_cut = [0] * (n + 1)

    for i in range(1, n + 1):
        max_profit = float('-inf')
        for j in range(1, i + 1):
            current_profit = prices[j - 1] + dp[i - j]
            if current_profit > max_profit:
                max_profit = current_profit
                first_cut[i] = j
        dp[i] = max_profit

    cuts = []
    remaining_length = n
    while remaining_length > 0:
        cut_len = first_cut[remaining_length]
        cuts.append(cut_len)
        remaining_length -= cut_len

    return dp[n], cuts


if __name__ == "__main__":
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    rod_length = len(prices)

    max_profit, optimal_cuts = rod_cutting(prices, rod_length)

    print(f"Rod Length: {rod_length}")
    print(f"Prices: {prices}")
    print(f"Maximum Profit: {max_profit}")
    print(f"Optimal Cuts: {optimal_cuts}")