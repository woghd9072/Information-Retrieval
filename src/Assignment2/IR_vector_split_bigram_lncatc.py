import  math,collections

def indexing(iF):
	posting,docText,docLen,N={},{},{},0.
	for line in open(iF,encoding='utf-8'):
		N+=1
		docNo,doc=line.rstrip().split('\t')
		docText[docNo]=doc[:30]
		L = list()
		for i in doc.split():
			if len(i) == 1:
				L += [i]
			else:
				L += [i[j-1:j+1] for j in range(1, len(i))]
		TF=collections.Counter(L)
		
		#docLen[docNo]=math.sqrt(sum([(1+math.log(tf))**2 for tf in TF.values()]))
		V=[]
		for tf in TF.values(): V.append((1+math.log(tf))**2)
		docLen[docNo]=math.sqrt(sum(V))
		
		for t,tf in TF.items():
			if t not in posting: posting[t]=[]
			posting[t].append((docNo,tf))
		# end for
	# end for
	
	#df={t:len(posting[t]) for t in posting}
	df={}
	for t in posting: df[t]=len(posting[t])
	
	return {'posting':posting,'docText':docText,'docLen':docLen,'N':N,'df':df}
# end def

def retrieval(Q,IndexDB):
	posting,docLen,N,df=IndexDB['posting'],IndexDB['docLen'],IndexDB['N'],IndexDB['df']
	score,qLen={},0.
	L = list()
	for i in Q.split():
		if len(i) == 1:
			L += [i]
		else:
			L += [i[j-1:j+1] for j in range(1, len(i))]
	qTF=collections.Counter(L)
	m = max(qTF.values())
	for qt,qtf in qTF.items():
		if qt not in posting: continue
		qtw=(0.5 + ((0.5 * qtf)/m))*math.log(N/df[qt])
		qLen+=qtw*qtw
		for docNo,dtf in posting[qt]:
			if docNo not in score: score[docNo]=0
			dtw=(1+math.log(dtf))
			score[docNo]+=qtw*dtw
		# end for
	# end for
	for docNo in score:
		score[docNo]/=math.sqrt(qLen)*docLen[docNo]
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