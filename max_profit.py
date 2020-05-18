"""121 - Best Time to Buy and Sell Stock"""
def maxProfit(prices):
        if len(prices) == 0:
           return 0

        buy_price = prices[0]
        sell_price = 0
        max_profit = 0

        for i in prices:
            if i < buy_price:
                buy_price = i
                sell_price = i
            if i > sell_price and max_profit < i - buy_price:
                sell_price = i
                max_profit = sell_price - buy_price

        return max_profit

if __name__ == '__main__':
    prices = [7,6,4,3,1]
    print(maxProfit(prices))