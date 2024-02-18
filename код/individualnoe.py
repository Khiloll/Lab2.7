#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")
    A = {"b", "d", "f", "g", "l", "u"}
    B = {"d", "e", "f", "m", "n", "z"}
    C = {"h", "i", "r", "x", "y"}
    D = {"a", "e", "f", "k", "r", "s", "x"}

    x = (A.intersection(B)).union(D)
    print(f"x = {x}")
    # дополнения множеств
    an = u.difference(A)
    bn = u.difference(B)
    y = (an.intersection(bn)).difference(C.union(D))
    print(f"y = {y}")
