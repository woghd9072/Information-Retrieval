import  math

def indexing(iF):
	posting,docText,docLen={},{},{}
	for line in open(iF,encoding='utf-8'):
		docNo,doc=line.rstrip().split('\t')
		docText[docNo]=doc[:30]
		L = list()
		for i in doc.split():
			if len(i) == 1:
				L += [i]
			else:
				L += [i[j-1:j+1] for j in range(1, len(i))]
		termSet=set(L)
		docLen[docNo]=math.sqrt(len(termSet))
		for t in termSet:
			if t not in posting: posting[t]=[]
			posting[t].append(docNo)
		# end for
	# end for
	return {'posting':posting,'docText':docText,'docLen':docLen}
# end def

def retrieval(Q,IndexDB):
	posting,docLen=IndexDB['posting'],IndexDB['docLen']
	score={}
	L = list()
	for i in Q.split():
		if len(i) == 1:
			L += [i]
		else:
			L += [i[j-1:j+1] for j in range(1, len(i))]
	termSet=set(L)
	for t in termSet:
		if t not in posting: continue
		for docNo in posting[t]:
			if docNo not in score: score[docNo]=0
			score[docNo]+=1 
		# end for
	# end for
	qLen=math.sqrt(len(termSet))
	for docNo in score:
		score[docNo]/=qLen*docLen[docNo]
	# end for
	return score
# end def

IndexDB=indexing('collection')
while(True):
	q=input('Query: ')
	score=retrieval(q,IndexDB)
	for docNo in sorted(score,key=score.get,reverse=True)[:10]:
		print('%.4f\t%s\t%s'%(score[docNo],docNo,IndexDB['docText'][docNo]))
	# end for
# end while