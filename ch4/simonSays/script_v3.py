#! /usr/bin/python3

print('User score:', (lambda x, y: max(filter(lambda z: x[:z] == y[:z], range(len(x)))))(input(), input()))
