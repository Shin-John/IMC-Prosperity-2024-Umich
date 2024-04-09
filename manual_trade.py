hashmap = {x: (x - 900) / 50 for x in range(900, 1001)}

def find_optimal_bids(hashmap):
    max_profit = 0
    optimal_low = 0
    optimal_high = 0
    selling_price = 1000
    for low_bid in range(900, 1001):
        for high_bid in range(low_bid + 1, 1001):
            profit = 0
            items_bought = 0
            for key, frequency in hashmap.items():
                if low_bid >= key:
                    profit += (selling_price - low_bid) * frequency
                    items_bought += frequency
                elif high_bid >= key:
                    profit += (selling_price - high_bid) * frequency
                    items_bought += frequency
            if profit > max_profit:
                max_profit = profit
                optimal_low = low_bid
                optimal_high = high_bid
    return optimal_low, optimal_high, max_profit

if __name__ == '__main__':
    optimal_low, optimal_high, max_profit = find_optimal_bids(hashmap)
    print(optimal_low, optimal_high, max_profit)
