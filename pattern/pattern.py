import sys

v = {}

array = {'baba', 'bebe', 'bibi', 'bobo', 'babu', 'baba', 'bubu', 'aeae', 'batatata', 'repolho', 'ratorato', 'tatatata'}

for w in array:

	count = 0
	aux = ''
	vw = {}

	for c in w:
		if count == 0:
			vw.update({c: count})
			aux += str(count)
			count += 1
		else:
			if vw.get(c) == None:
				vw.update({c: count})
				aux += str(count)
				count += 1
			else:
				aux += str(vw.get(c))

	v.update({w: aux})


print (v)
