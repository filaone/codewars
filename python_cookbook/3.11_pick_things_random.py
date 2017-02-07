#!/usr/bin/python
#-*- coding:utf-8 -*- 

import random
values = [1,2,3,4,5,6,7]
print('random.choice(values)', random.choice(values))
print('random.choice(values)', random.choice(values))
print('random.choice(values)', random.choice(values))
print('random.choice(values)', random.choice(values))
print('random.choice(values)', random.choice(values))
print('random.choice(values)', random.choice(values))

print('random.sample(values,2)', random.sample(values,2))
print('random.sample(values,2)', random.sample(values,2))
print('random.sample(values,2)', random.sample(values,2))
print('random.sample(values,2)', random.sample(values,2))


# shuffle items
random.shuffle(values)
print('random.shuffle(values) and print values', values)


print('random.randint(0,10)', random.randint(0,10))
print('random.randint(0,10)', random.randint(0,10))
print('random.randint(0,10)', random.randint(0,10))
print('random.randint(0,10)', random.randint(0,10))


print('random.random()', random.random())
print('random.random()', random.random())
print('random.random()', random.random())
print('random.random()', random.random())
print('random.random()', random.random())


# N random-bits expressed as an integer
print('random.getrandbits(200)', random.getrandbits(200))

random.seed(12345)
print('random.choice(values)', random.choice(values))
random.seed(12345)
print('random.choice(values)', random.choice(values))
random.seed(12345)
print('random.choice(values)', random.choice(values))
random.seed(12345)
print('random.choice(values)', random.choice(values))
random.seed(12345)
print('random.choice(values)', random.choice(values))
random.seed(b'bytedata')
print('random.choice(values)', random.choice(values))
random.seed(b'bytedata')
print('random.choice(values)', random.choice(values))
random.seed(b'bytedata')
print('random.choice(values)', random.choice(values))
random.seed(b'bytedata')
print('random.choice(values)', random.choice(values))
random.seed(b'bytedata')
print('random.choice(values)', random.choice(values))

import ssl
print('ssl.RAND_bytes()', ssl.RAND_bytes(2))
