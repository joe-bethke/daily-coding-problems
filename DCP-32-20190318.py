"""
This problem was asked by Jane Street.
Suppose you are given a table of currency exchange rates, represented as a 2D array.
Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make,
starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.
There are no transaction costs and you can trade fractional quantities.
"""

exchange_rates = [
    [   1,    2,  4],
    [ 0.5,    1,  2],
    [0.25, 0.55,  1]
]


def has_arbitrage(exchange_rates):
    # Returns True if there is an arbitrage in the given exchange rates
    return any(exchange_rates[i][j] > (1 / exchange_rates[j][i]) and exchange_rates[i][j] > 0
               for i in range(len(exchange_rates))
               for j in range(len(exchange_rates)))


assert has_arbitrage(exchange_rates)
print(has_arbitrage([
    [1, 2, 4],
    [0.5, 1, 2],
    [0.25, 0.5, 1]
]))
