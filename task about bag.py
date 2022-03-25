#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Задача о рюкзаке
"""

def bug(cap, values, weights):
    items = []
    for i in range(len(values)):
        itemInfo = {
            'value_for_one': values[i] / weights[i],
            'weight': weights[i]
        }
        if len(items) == 0:
            items.append(itemInfo)
        else:
            k = 0
            while k < len(items) and items[k]['value_for_one'] > itemInfo['value_for_one']:
                k += 1
            items.insert(k, itemInfo)
    total = 0
    cap_left = cap
    for item in items:
        if cap_left - item['weight'] >= 0:
            total += item['weight'] * item['value_for_one']
            cap_left -= item['weight']
        elif cap_left > 0:
            total += item['value_for_one'] * cap_left
            cap_left = 0
    return total


if __name__=='__main__':
    cap = 60
    values = [60, 100, 120]
    weights = [20, 50, 30]
    print(bug(cap, values, weights))
