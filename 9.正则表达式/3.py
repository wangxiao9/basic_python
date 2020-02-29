'''
1. 数量词
 - {}
 - * ： 匹配0个或多个
 - ？: 匹配0个或者1个
 - + : 匹配一个或者多个
'''
import re

a = 'python java php c# C'

# ep1: 匹配python java php
print(re.findall('\S{3,6}', a))

b = 'pytho3python$$pythonn^pythonnn '
print(re.findall('python*', b))
print(re.findall('python?', b))
print(re.findall('python+', b))