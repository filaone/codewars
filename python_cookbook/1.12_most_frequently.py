#!/usr/bin/python
#-*- coding:utf-8 -*-

# 1.12 Determining the Most Frequently Occurring Items in a Sequence
# use collections' Counter

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
print(word_counts.most_common(3))
print(word_counts)

morewords = ['Awhy','are','you','not','looking','in','my','eyes']
for word in morewords:
    word_counts[word] += 1

moreword_counts = Counter(morewords)
print('moreword_counts : ', moreword_counts)
print('word plus  more : ', word_counts + moreword_counts)
print('word del more : ', word_counts - moreword_counts)

print(word_counts['eyes'])
print(word_counts['Awhy'])

def my_Counter(items):
    count = Counter()
    for item in items:
        count[item] += 1
    return sorted(count.items(), key=lambda k:k[1])

print(my_Counter(words))
