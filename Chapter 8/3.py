def magic_num_search(array, start, end):
    if start > end:
        return False, -1
    mid = (start+end)//2
    mid_number = array[mid]
    if mid_number == mid:
        return True, mid
    if start == end:
        return False, -1
    if mid_number < mid:
        return magic_num_search(array, mid+1, end)
    else:
        return magic_num_search(array, start, mid-1)

array = [0, 2, 3,5,6]
print(magic_num_search(array, 0, len(array)-1))