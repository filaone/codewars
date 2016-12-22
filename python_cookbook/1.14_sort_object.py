#!/usr/bin/python
#-*- coding:utf-8 -*- 


# 1.14 Sorting Objects Without Native Comparison Support

from operator import attrgetter

class User:
    def __init__(self, user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User({})'.format(self.user_id)

if __name__ == '__main__':
    users = [User(23), User(3), User(99)]
    print(sorted(users, key = lambda k:k.user_id))
    print(sorted(users, key = attrgetter('user_id')))
    print(min(users, key = attrgetter('user_id')))
