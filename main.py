def min_index(arr):
    return arr.index(min(arr))


def sum_between_negatives(arr):
    neg = [i for i, x in enumerate(arr) if x < 0]
    if len(neg) < 2:
        return 0
    return sum(arr[neg[0] + 1:neg[1]])


def transform_array(arr):
    return [x for x in arr if abs(x) <= 1] + [x for x in arr if abs(x) > 1]


def main():
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(float(input()))

    print(min_index(arr))
    print(sum_between_negatives(arr))
    print(transform_array(arr))


main()
