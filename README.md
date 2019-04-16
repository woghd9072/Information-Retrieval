# Information-Retrieval

## 정보검색 with Python

## 개발환경
|Tool|Version|
|:---:|:---:|
|Python|Python 3.7.2|
|OS|Window 10|
|Edit|Notepad ++|

## 주차로 진행

### 1주차
- 정보검색
  - 대량의 정보 모음으로부터 사용자의 정보 요구(Information Need)를 만족하는 자료를 찾는 것
  - 정보 요구(Information Need)를 질의(Query)로 작성 시 정보 손실이 발생한다.
  1. 사용자는 객체 모음으로부터 원하는 정보가 있으며 그 정보를 질의로 표현한다.
  2. 시스템은 질의를 만족하는 객체(들)을 찾아 사용자에게 유용한 형식으로 제시한다.
  3. 사용자는 제시된 객체들 중 어떤 것이 자신의 정보 요구에 적합한 지를 결정한다.
- 질의-문서 유사도
  - TF
    - 특정한 하나의 문서 내에 출현한 특정한 용어의 출현 횟수
  - DF
    - 특정한 용어가 출현한 문서의 개수
  - CF
    - 특정한 용어가 문서 집합 전체에서 출현한 횟수
  - IDF
    - 역문헌 빈도수
    $$ idf(t) = log({N\over df(t)}) $$
  - 가중치
    $$ w(t,D) = {tf(t,D) * idf(t)\over Length(D)} $$
### 2주차
- 색인
- Stemming
  - Porter's stemmer
    ex) automate → autom
- n-gram
  ex) 경성대학교 → 경성,성대,대학,학교
- 역파일 색인(Inverted Indexing)
  - df나 tf로 정렬 가능하다

|문서 번호|출현 용어|→|출현 용어|문서 번호|
|:---:|:---:|:---:|:---:|:---:|

### 3주차
- 검색모델
  - 불리언 모델
  - 벡터 모델

### 4주차
- Precision
- Recall

### 5주차
- F지표
- F1지표

### 6주차
- Precision-Recall Curve
- MAP
- Precision at K
- R-precision
