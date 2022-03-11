words = input.split()

word_counts = {}
for word in words:
	words_counts[word] = word_counts.get(word, 0) + 1

for word in words:
	print(word, word_count[word])