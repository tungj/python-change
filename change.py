def change(amt):
    coins = [100,50,20,10,5,1]
    used = [0] * len(coins)
    remaining = amt
    for idx, coin in enumerate(coins):
        if (remaining >= coin):
            coinCount = remaining // coin
            used[idx] = coinCount
            remaining = remaining - coinCount * coin

    return [x for x in zip(used, coins) if x[0] > 0]


print(change(116))
# [(1, 100), (1, 10), (1, 5), (1, 1)]
print(change(799))
# [(7, 100), (1, 50), (2, 20), (1, 5), (4, 1)]

