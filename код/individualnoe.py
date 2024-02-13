#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")
    A = {"a", "b", "h", "k", "o", "r"}
    B = {"b", "g", "h", "l", "s"}
    C = {"k", "l", "z"}
    D = {"g", "i", "p", "q", "u", "v"}
    x = (A.intersection(B)).union(D)
    print(f"x = {x}")
    # дополнения множеств
    an = u.difference(A)
    bn = u.difference(B)
    y = (an.intersection(bn)).difference(C.union(D))
    print(f"y = {y}")
