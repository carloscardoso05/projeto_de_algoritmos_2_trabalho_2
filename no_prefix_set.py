#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

class NoTrie:
    def __init__(self):
        self.filhos = {}
        self.eh_fim: bool = False


class Trie:
    def __init__(self):
        self.raiz: NoTrie = NoTrie()

    def inserir(self, palavra):
        node = self.raiz
        for char in palavra:
            if char not in node.filhos:
                node.filhos[char] = NoTrie()
            node = node.filhos[char]
            if node.eh_fim:
                return True
        if node.filhos:
            return True
        node.eh_fim = True
        return False


def noPrefix(words):
    trie = Trie()
    for word in words:
        if trie.inserir(word):
            print("BAD SET")
            print(word)
            return
    print("GOOD SET")

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
