def paren(n):
    results = []
    recursive_paren_permutation(n, "(", 1, 0, results)
    return results


def recursive_paren_permutation(n, perm_so_far, open_par_cnt, closed_par_cnt, results):
    if open_par_cnt == closed_par_cnt and open_par_cnt == n:
        results.append(perm_so_far)

    if open_par_cnt < n:
        recursive_paren_permutation(n, perm_so_far + "(", open_par_cnt + 1, closed_par_cnt, results)
    if closed_par_cnt < open_par_cnt:
        recursive_paren_permutation(n, perm_so_far + ")", open_par_cnt, closed_par_cnt + 1, results)


res = paren(4)
for r in res:
    print(r)