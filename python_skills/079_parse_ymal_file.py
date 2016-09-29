#!/usr/bin/python
#-*- coding:utf-8 -*-

import  yaml

with open("./addon/example.yaml","r") as stream:
    try:
        print(yaml.load(stream))
    except yaml.YAMLError as exc:
        print exc


# you can also use the ruamel.yaml
