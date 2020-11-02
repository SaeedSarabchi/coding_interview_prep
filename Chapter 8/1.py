def rec_count(n):
    if n==0:
        return 1
    if n<0:
        return 0

    return rec_count(n-1) + rec_count(n-2) + rec_count(n-3)

def dyn_count(n, counts=None):
    if n==0:
        return 1
    if n<0:
        return 0
    if counts is None:
        counts = {}
    if n in counts:
        return counts[n]

    counts[n] =  dyn_count(n-1, counts) + dyn_count(n-2, counts) + dyn_count(n-3, counts)
    return counts[n]

print(dyn_count(50))
print(rec_count(50))


