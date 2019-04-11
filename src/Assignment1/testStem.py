from stemming.porter2 import stem

s = 'automate automated automates automating automation operate operating operates operation operative operatives operational'
L = s.split()
for e in L:
	print(stem(e))
