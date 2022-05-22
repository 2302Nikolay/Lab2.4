#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys

if __name__ == '__main__':

    a = list(input("Введите список: ").split())
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    elem = input("Введите элемент, индекс которого необходимо найти: ")
    if elem in a:
        print(a.index(elem))
    else:
        print("Данный элемент отсутствует в списке")
