#!/usr/bin/python
#-*- coding:utf-8 -*-

prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}
 
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }

if __name__ == "__main__":
    p1 = {key:value for key,value in prices.items() if value > 200}
    print(p1)
    p2 = {key:value for key,value in prices.items() if key in tech_names}
    print(p2)
    p3 = {key:prices[key] for key in prices.keys() & tech_names}
    p4 = {key:prices[key] for key in tech_names if key in prices.keys()}
    print(p3)
    print(p4)
    # create a sequence of tuples
    p5 = ((key,value) for key,value in prices.items() if value > 200)
    print(p5)
    print(dict(p5))
