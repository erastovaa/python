def quick_sort(data):
    less = []
    equal = []
    greater = []
    if len(data) > 1:
        pivot = data[0]
        for i in data:
            if i < pivot:
                less.append(i)
            if i == pivot:
                equal.append(i)
            if i > pivot:
                greater.append(i)
        return quick_sort(less) + equal + quick_sort(greater)
    else:
        return data


if __name__ == '__main__':
    n = int(input())
    data = list(map(int, input().split()))
    print(' '.join(map(str, quick_sort(data))))
