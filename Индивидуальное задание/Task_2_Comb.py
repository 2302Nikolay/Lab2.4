#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys

if __name__ == '__main__':

    a = list(map(int, input("Введите список из целых элементов: ").split()))
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    a_min = abs(a[0])
    i_min = 0
    for i in a:
        if abs(i) < a_min:
            a_min = abs(i)
            i_min = a.index(i)

    print("Минимальный по модулю элемент: ", a[i_min])

    ind = a.index(0)
    s = 0
    for n, i in enumerate(a):
        if n > ind:
            s += i
    print("Сумма элементов после нуля: ", s)
