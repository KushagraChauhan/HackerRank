#this is the left rotation question

n, k = map(int, input().strip().split(' '))
c = a = [int(i) for i in input().split()]


def array_left_rotation(a, n, k):
    for i in range(k, n + k):
        if i < n:
            print(a[i], end=' ')
        else:
            print(a[i - n], end=' ')


array_left_rotation(a, n, k)
