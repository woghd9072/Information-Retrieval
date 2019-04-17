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
  - 불리언 모델(Boolean Model)
    1. Query : 피연산자인 용어들을 불리언 연산자(AND,OR,NOT)로 표현 ex) 북한 AND 미사일
    2. Document : 용어들의 집합
    3. Retrieval : 각 query term T에 대해 T를 포함하는 문서집합 S를 대응시키고, 불리언 수식으로 표현된 query를 만족하는 집합 R을 찾아, R에 포함된 문서들을 사용자에게 제시
  - 벡터 모델(Vector space Model)
    1. 벡터공간 : 각 용어를 차원으로 갖는 벡터공간 (크기 n의 용어 집합에 대해 n-차원 벡터공간이 정의됨)
    2. Query : 벡터공간 내의 한 벡터 (질의 벡터)
    3. Document : 벡터공간 내의 한 벡터 (문서 벡터)
    4. Retrieval : 각 문서벡터에 대해 질의벡터와 유사한 정도를 계산하여 유사도순으로 사용자에게 제시
  - 질의-문서 유사도(코사인 유사도)
    1. 질의벡터와 문서벡터의 사잇각이 적을수록 1에 가까운 값을, 사잇각이 클수록 0에 가까운 값을 부여하는 수식
  - 이진 벡터 표현
    1. 질의/문서 내 용어 출현 여부만을 고려해서 출현 용어에 대응하는 벡터 성분을 1, 아니면 0을 할당하는 방식
  - TF 벡터 표현
    1. 질의/문서 내 출현 횟수를 고려하여 용어에 대응하는 벡터성분에 해당 용어의 출현 횟수를 할당하는 방식
  - IDF 벡터 표현
    1. 각 용어에 대해 문서집합에서 용어가 출현한 문서 수에 반비례하는 값을 해당 용어에 대응하는 벡터성분에 할당하는 방식
  - TF-IDF 벡터 표현
    1. 용어의 문서 내 출현 빈도인 TF와 문서집합 내 역문헌빈도인 IDF를 동시에 고려하는 벡터성분 표현
    2. 벡터공간모델의 대표적 용어 가중치 부여 방식

### 4주차
- Precision(정확률)
  $$ Precision = {검색된 문서중 적합문서의 수\over 검색된 문서의 수} $$
- Recall(재현율)
  $$ Recall = {검색된 문서중 적합문서의 수\over 적합문서의 수} $$

### 5주차
- F지표

$$ F = {1\over\alpha{1\over P}+(1-\alpha){1\over R}} $$

- F1지표

$$ F1(\alpha=1/2) = {1\over\alpha{1\over P}+(1-\alpha){1\over R}}
= {1\over {1\over 2}{1\over P}+(1-{1\over 2}){1\over R}} = {2PR\over P+R} $$


### 6주차
- Precision-Recall Curve
- MAP
- Precision at K
- R-precision

### 7주차
- NDCG
- Pooling technique
- Pivoted Document Length Normalization
