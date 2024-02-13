#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Решите задачу: подсчитайте количество гласных в строке,
# введенной с клавиатуры с использованием множеств.

if __name__ == "__main__":
    vowels_all = {'a', 'e', 'i', 'o', 'u', 'y',
                  'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'}

    string = input("Введите строку: ")

    count = len([i for i in string.lower() if i in vowels_all])

    print("Количество гласных в строке:", count)
