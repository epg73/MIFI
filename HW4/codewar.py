
def positive_sum(arr):
    c=0
    if arr:
        for a in arr:
            if a:
                c+=a
    else:
        return 0
    return c

print(positive_sum([]))