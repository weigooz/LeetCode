#Pair Sum

def pair_sum(arr, k):
    items = set(arr)
    pair = {}
    same_value_count = 0
    for item in items:
        if (k-item) in items:
            pair.update({k-item:item})
            if k-item == item: same_value_count +=1
        else:
            continue
    return (len(pair)-same_value_count)/2 + same_value_count

def pair_sum2(arr, k):
    items = set(arr)
    pair = []
    for item in items:
        if (k-item) in items:
            if (k-item) not in pair:
                pair.append(item)
        else:
            continue
    return len(pair)
