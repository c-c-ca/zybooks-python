#! /usr/bin/python3

user_score = 0
simon_pattern = input()
user_pattern = input()

''' Your solution goes here '''
for simon_letter, user_letter in zip(simon_pattern, user_pattern):
	if simon_letter != user_letter: break
	user_score += 1

print('User score:', user_score)