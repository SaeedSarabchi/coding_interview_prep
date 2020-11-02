def calc_coins(n):
    prefix = (0,0,0,0)
    prefixes = set()
    return rec_coins_cnt(n, prefix, prefixes)

#Terrible!! O(4^n) plus space complexity of O(4^n) as well.
def rec_coins_cnt(n, prefix, prefixes):
    if n == 0:
        return 1
    if n < 0:
        return 0
    sum = 0
    for pick in (25, 10, 5, 1):
        new_prefix = None
        if pick==25: new_prefix = (prefix[0]+1,prefix[1],prefix[2],prefix[3])
        elif pick==10: new_prefix = (prefix[0],prefix[1]+1,prefix[2],prefix[3])
        elif pick==5: new_prefix = (prefix[0],prefix[1],prefix[2]+1,prefix[3])
        elif pick==1: new_prefix = (prefix[0],prefix[1],prefix[2],prefix[3]+1)
        if new_prefix not in prefixes:
            prefixes.add(new_prefix)
            sum += rec_coins_cnt(n - pick, new_prefix, prefixes)
    return sum


def calc_coins2(n):
    coin_set = [25,10,5,1]
    return rec_coins_cnt2(n, coin_set)

#better than rec_coins_cnt2,
#time complexity is O(
# since space complexity is O(1)
def rec_coins_cnt2(n, coin_set):
    #todo: base case
    if n<0:
        return 0
    if n==0:
        return 1
    if len(coin_set)==0:
        return 0

    coin = coin_set[0]
    sum = 0
    for i in range(n//coin+1):
        rem = n-i*coin
        sum += rec_coins_cnt2(n-i*coin, coin_set[1:])
    return sum


def calc_coins_memo(n):
    coin_set = [25,10,5,1]
    memo = {}
    return rec_coins_cnt_memo(n, coin_set, memo)



def rec_coins_cnt_memo(n, coin_set, memo):
    #todo: base case
    if n<0:
        return 0
    if n==0:
        return 1
    if len(coin_set)==0:
        return 0

    coin = coin_set[0]
    sum = 0
    for i in range(n//coin+1):
        rem = n-i*coin
        if (rem,coin) in memo:
            sum += memo[(rem,coin)]
        else:
            memo[(rem,coin)] = rec_coins_cnt_memo(n-i*coin, coin_set[1:], memo)
            sum += memo[(rem,coin)]
    return sum

n = 400
print(calc_coins_memo(n))
print(calc_coins2(n))
print(calc_coins(n))
