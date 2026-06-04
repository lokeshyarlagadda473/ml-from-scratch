def derivative_numerical(f, x, h=1e-7):
    return (f(x + h) - f(x)) / h

result = derivative_numerical(lambda x: x**2, 3)
# Should give approximately 6.0

import math

print(derivative_numerical(math.sin, 0))      # ~1.0
print(derivative_numerical(math.exp, 0))      # ~1.0
print(derivative_numerical(lambda x: x**3, 2)) # ~12.0