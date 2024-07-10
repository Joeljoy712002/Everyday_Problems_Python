# max profit


def maxProfit(price):
    n = len(price)
    if n <= 1:
        return 0
    
    max_profit = 0
    min_price = price[0]

    for i in range(1, n):
        if price[i] > min_price:
            max_profit += price[i] - min_price
        min_price = price[i]

    return max_profit

if __name__ == '__main__':
     array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
     print(maxProfit(array))
