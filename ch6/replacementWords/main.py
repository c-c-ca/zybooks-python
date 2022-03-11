#! /usr/bin/python3

originals_and_replacements = input().split()
sentence = input()

originals = originals_and_replacements[0::2]
replacements = originals_and_replacements[1::2]

for original, replacement in zip(originals, replacements):
	sentence = sentence.replace(original, replacement)

print(sentence)
