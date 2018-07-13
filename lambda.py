def multipliers():
    return [lambda x : i * x for i in range(4)]

print([m(2) for m in multipliers()])

## http://composingprograms.com/pages/16-higher-order-functions.html#lambda-expressions
## [6, 6, 6, 6]