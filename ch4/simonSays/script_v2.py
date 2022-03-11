#! /usr/bin/python3

print('User score:', (lambda x, y: max([i for i in range(len(x)) if x[:i] == y[:i]]))(input(), input()))

