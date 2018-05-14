def word_tally(phrase):
	words= phrase.split(" ")
	tally={}
	for word in words:
		if word not in tally:
			tally[word]=0
		tally[word]+=1
	print (tally)
	return tally
phrase = "to be or not to be"
word_tally(phrase)
	