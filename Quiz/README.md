#Quiz

## 1주차 Quiz

1. 문서검색시스템은 ____에 적합한 _____를 검색한다.
  → 질의(Query), 문서(Document)

2. 정보검색에서 사용자의 정보요구가 표출된 것을 지칭하는 용어는?
  → 질의(Query)

3. IR 시스템은 문서집합을 검색 시점 이전에 ______해 둔다.
  → 색인(Indexing)

4. 다음 문서 집합 {D1, D2, D3, D4}에 대해 아래 값들을 채우시오.
  D1 = [축구, 축구화, 축구공]       D2 = [축구, 축구, 경기, 관중, 응원]
  D3 = [축구, 축구, 축구, 월드컵, 유럽리그]         D4 = [축구, 야구, 농구, 배구]
  tf(D2,축구) = 2
  tf(D3,축구) = 3
  df(축구) = 4
  cf(축구) = 7
  idf(축구) = log(4/4)

5. 다음 문서 집합 {D1, D2}와 질의 Q와의 유사도를 계산하시오.(tf, idf, length 사용)
  Q = 축구    D1 = [축구, 축구, 용품]     D2 = [축구, 경기, 응원]
  → sim(Q,D1) = tf*idf/length = 2*1/3
  → sim(Q,D2) = tf*idf/length = 1*1/3

6. 다음 문서 집합 {D1, D2}와 질의 Q와의 유사도를 계산하시오.(tf, idf, length 사용)
  Q = 축구    D1 = [축구, 축구, 용품]     D2 = [축구, 축구, 선수, 올림픽]
  → sim(Q,D1) = tf*idf/length = 2*1/3
  → sim(Q,D2) = tf*idf/length = 2*1/4

7. 다음 문서 집합 {D1, D2, D3, D4, D5}와 질의 Q와의 유사도를 계산하시오.(tf, idf, length 사용)
  Q = 날씨, 속보
  D1 = [날씨]   D2 = [속보]   D3 = [날씨]   D4 = [날씨]   D5 = [날씨]
  → sim(Q,D1) = tf*idf/length = (1*5/4)/1
  → sim(Q,D2) = tf*idf/length = (1*5/1)/1
  → sim(Q,D3) = tf*idf/length = (1*5/4)/1
  → sim(Q,D4) = tf*idf/length = (1*5/4)/1
  → sim(Q,D5) = tf*idf/length = (1*5/4)/1

8. 다음 문서 집합 {D1, D2, D3, D4, D5}와 질의 Q와의 유사도를 계산하시오.(tf, idf, length 사용)
  Q = 날씨, 속보
  D1 = [날씨, 날씨]   D2 = [속보]   D3 = [날씨, 속보]   D4 = [날씨]   D5 = [날씨]
  → sim(Q,D1) = tf*idf/length = (2*5/4)/2
  → sim(Q,D2) = tf*idf/length = (1*5/2)/1
  → sim(Q,D3) = tf*idf/length = (1*5/4)/2 + (1*5/2)/2
  → sim(Q,D4) = tf*idf/length = (1*5/4)/1
  → sim(Q,D5) = tf*idf/length = (1*5/4)/1

9. 다음 용어에 대한 음절 2-gram 색인어를 모두 추출하시오.
  임시정부에서는 → 임시, 시정, 정부, 부에, 에서, 서는
