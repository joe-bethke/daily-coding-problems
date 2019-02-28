"""
This problem was asked by Google.
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.
Hint: The basic equation of a circle is x2 + y2 = r2.
"""
from math import pi, sqrt
from random import random


attempts = 1000
my_pi = ((sum(1 for _ in range(attempts) if sqrt(random()**2 + random()**2) < 1) /
          attempts) * 4)
print(attempts, my_pi)


my_pi = 0
attempts = 1
while abs(pi - my_pi) > .001:
    my_pi = ((sum(1 for _ in range(attempts) if sqrt(random()**2 + random()**2) < 1) /
              attempts) * 4)
    attempts += 1

print(attempts, my_pi)
