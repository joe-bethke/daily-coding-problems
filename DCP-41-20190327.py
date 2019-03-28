"""
This problem was asked by Facebook.

Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs,
and a starting airport, compute the person's itinerary. If no such itinerary exists, return null.
If there are multiple possible itineraries, return the lexicographically smallest one.
All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A',
you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary.
However, the first one is lexicographically smaller.
"""
from collections import Counter


def solve(flights, start):
    flight_count = Counter([airport for flight in flights for airport in flight])

    def valid_itin(itin):
        return ((len(itin) == len(flights) + 1) and
                all(itin_count == (flight_count[airport] - 1) for airport, itin_count in Counter(itin).items()))

    starts = [flight for flight in flights if flight[0] == start]
    itins = [[start]]
    while not any(map(valid_itin, itins)):
        new_itins = list()
        for itin in itins:
            current_airport = itin[-1]
            for flight in flights:
                if flight[0] == current_airport:
                    new_itins.append(itin + [flight[1]])
        if new_itins:
            itins = new_itins
        else:
            return None
    return sorted([itin for itin in itins if valid_itin(itin)], key=lambda itin: "".join(itin))[0]

itin = solve([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], "A")
assert itin == ['A', 'B', 'C', 'A', 'C']

itin = solve([('A', 'C'), ('B', 'C')], 'A')
assert itin is None
