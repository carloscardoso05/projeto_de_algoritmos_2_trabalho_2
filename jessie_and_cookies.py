#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

from typing import List

def construir_heap(heap: List[int]) -> None:
    n = len(heap)
    for i in range(n // 2 - 1, -1, -1):
        j = i
        tamanho = n
        while True:
            esquerda = (j << 1) + 1  # 2*j + 1
            direita = esquerda + 1     # 2*j + 2
            menor = j
            if esquerda < tamanho and heap[esquerda] < heap[menor]:
                menor = esquerda
            if direita < tamanho and heap[direita] < heap[menor]:
                menor = direita
            if menor == j:
                break
            heap[j], heap[menor] = heap[menor], heap[j]
            j = menor

def remove_min(heap: List[int]) -> int:
    tamanho = len(heap)
    min_val = heap[0]
    last_val = heap.pop()
    if tamanho > 1:
        heap[0] = last_val
        j = 0
        tamanho = len(heap)
        while True:
            esquerda = (j << 1) + 1
            direita = esquerda + 1
            menor = j
            if esquerda < tamanho and heap[esquerda] < heap[menor]:
                menor = esquerda
            if direita < tamanho and heap[direita] < heap[menor]:
                menor = direita
            if menor == j:
                break
            heap[j], heap[menor] = heap[menor], heap[j]
            j = menor
    return min_val

def inserir(heap: List[int], valor: int) -> None:
    heap.append(valor)
    i = len(heap) - 1
    while i:
        pai = (i - 1) >> 1  # Equivalent to (i - 1) // 2
        if heap[pai] > heap[i]:
            heap[pai], heap[i] = heap[i], heap[pai]
            i = pai
        else:
            break

def cookies(k: int, A: List[int]) -> int:
    construir_heap(A)
    operacoes = 0

    while A and A[0] < k:
        if len(A) < 2:
            return -1
        s1 = remove_min(A)
        s2 = remove_min(A)
        inserir(A, s1 + 2 * s2)
        operacoes += 1

    return operacoes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
