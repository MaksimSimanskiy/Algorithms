#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Алгоритм Хаффмана
"""

class Node(object):
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.lchild = None
        self.rchild = None

def findTheCharFrequency(text):
    result = dict()
    with open(text, 'r') as f:
        for line in f.readlines():
            line = line.lower()
            for i in line:
                if i.isalpha():
                    if i in result:
                        result[i] += 1
                    else:
                        result.update({i:1})
    return result


class HuffmanTree(object):

    def __init__(self, char_Weights):
        self.Leaf = [Node(k,v) for k, v in char_Weights.items()]
        while len(self.Leaf) != 1:
            self.Leaf.sort(key=lambda node:node.value, reverse=True)
            n = Node(value=(self.Leaf[-1].value + self.Leaf[-2].value))
            n.lchild = self.Leaf.pop(-1)
            n.rchild = self.Leaf.pop(-1)
            self.Leaf.append(n)
        self.root = self.Leaf[0]
        self.Buffer = list(range(10))

    def Hu_generate(self, tree, length):
        node = tree
        if (not node):
            return
        elif node.name:
            print(node.name + ' - Кодировка Хаффмана:', end='')
            for i in range(length):
                print(self.Buffer[i], end='')
            print('\n')
            return
        self.Buffer[length] = 0
        self.Hu_generate(node.lchild, length + 1)
        self.Buffer[length] = 1
        self.Hu_generate(node.rchild, length + 1)

    def get_code(self):
        self.Hu_generate(self.root, 0)


if __name__=='__main__':
    text = r'file.txt'
    result = findTheCharFrequency(text)
    print(result)
    tree = HuffmanTree(result)
    tree.get_code()
