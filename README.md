# Information-Retrieval

## 정보검색 with Python

## 목적
- 정보검색 강의 과목 정리 및 Review
- Python 과제를 통한 Python 공부

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

- Precision, Recall, F1
  - 검색 문서 집합 단위의 성능 평가 지표
  - 검색 문서들은 적합도 순으로 정렬되어 있지 않다고 가정
  - 순위화된 형태로 검색 문서가 제시되는 경우를 고려한 성능 평가 지표가 필요함

### 6주차
- Precision-Recall Curve
  - 순위화된 검색 결과 리스트의 각 순위 지점에 대해, Recall과 Precision 값을 계산하여 2차원 좌표에 표시
  - 단순 Precision-Recall Curve의 문제 : 일반적으로 톱니모양(sawtooth) 그래프 발생
- Interpolated Precision-Recall Curve
  - 순위화된 검색 결과 리스트의 각 순위 지점에 대해, Recall과 Interpolated Precision 값을 계산하여 2차원 좌표에 표시
  - 좀 더 단순화시켜 특정 재현률 지점들에 대해서만 보간 정확률을 계산할 수 있음
  - Interpolated Precision(보간정확률) : 특정 recall level r에서의 보간정확률은 r이상의 모든 recall level에서의 최대 정확률로 정의된다.
- Averaged 11-point Precision/Recall Graph
  - 각 query에 대해 11개 각 재현율 수준(0.0 ~ 1.0)에서의 보간정확률들을 구하고, 같은 재현율 수준에 대해 서로 다른 질의의 보간정확률들의 평균을 구하여 2차원 좌표에 표시
- MAP
  - AP(Average Precision) : 하나의 query에 대해 얻어진 검색문서리스트에서 적합문서가 발견된 지점들에 대해서만 Precision을 계산하여 총 적합문서수로 평균한 것
  - MAP(Mean Average Precision) : 서로 다른 query들에 대해 각 query의 Average Precision들을 평균한 것
- Precision at K
  - 상위 K개의 문서만을 고려하여 정확률을 계산한 것
  - 장점 : 적합문서집합의 크기를 추정할 필요가 없음
  - 단점 : 평가지표들 중 가장 불안정, 총 적합문서 수가 성능에 큰 영향을 미침
- R-precision
  - 한 query에 대한 총 적합문서 수(R)와 같은 수의 검색문서집합이 얻어진 지점에서의 Precision을 계산
  - 질의마다 다른 적합문서집합의 크기에 유연하게 반응함
  - R-precision값은 Precision이면서 동시에 Recall이다. (정확률과 재현율이 같은 지점)

### 7주차
- NDCG
  - 다중 적합도가 부여된 상황을 위해 고안됨
    1. 이진적합도 → 적합문서(1), 부적합문서(0)
    2. 다중적합도 → 부적합(0), 부분적 적합(1), 적합(2), 상당부분 적합(3)
  - Precision at K처럼 상위 K개 검색문서에 대해 계산됨
  - G(Gain) : 사용자가 얼마나 이득을 얻었는가를 나타냄(적합도 점수)
  - CG(Cumulative Gain) : Gain 값을 모두 합산한 것
    1. 단순 누적한 값이다.
    2. 리스트 내 각 문서의 순위를 반영하지 못함 → CG값으로 어떤 검색 시스템이 좋은지 판별 불가
  - DCG(Discounted Cumulative Gain) : Discounted된 Gain 값을 합산한 것
    1. CG에 단점을 보완
    2. 문서의 순위를 고려하여 Discount 시킴
    3. 질의별 검색리스트/적합문서집합의 크기 차이를 반영하지 못함
  - NDCG : DCG를 정규화한 것
    1. 이진적합도인 경우

    $$ NDCG = {DCG\over max(DCG)} $$

    2. 다중적합도인 경우

    $$ NDCG_k = {DCG_k\over IDCG_k} $$

    3. IDCG : 가장 이상적인 시스템의 DCG값    
- Pooling technique
  - Relevance Judgements 구축 방법
  - 서로 다른 검색 알고리즘을 통해 얻어진 서로 다른 K개(K=50~200)의 문서들의 (중복제거) 모음을 대상으로 수작업 적합성 판단 수행
  - 대용량 문서집합에 대한 현실적 대응
- Pivoted Document Length Normalization

### 8주차(시험)

### 9주차
- 확률(Probability) : 사건의 가능성을 수치화(0에서 1사이의 값)하여 나타낸 것
  - 임의시행(experiment, random trial) : 결과를 만드는 임의 실험
  - 시행결과(outcome) : 임의시행의 결과
  - 표본공간(sample space) : 모든 가능한 시행결과들의 집합
  - 사건(event) : 확률이 부여되어야 할 시행결과들의 집합, 표본공간의 부분집합
  - 단위사건(elementary event) : 단일 결과로만 이루어진 사건
- Kolmogorov 확률 : 다음 공리 하에서 임의 사건을 [0,1] 사이 값으로 사상하는 함수
  - Kolmogorov axiom 1
    - 임의 사건의 확률은 0에서 1사이의 값이다.
  - Kolmogorov axiom 2
    - 모든 단위사건의 확률의 합은 1이다.
    - 공사건(단위결과를 하나도 포함하지 않는 사건, 즉 공집합)의 확률은 0이다.
  - Kolmogorov axiom 3
    - 서로 배반인 사건들의 확률은 각 배반사건의 확률들의 합과 같다.
- 사건
  - 곱사건(교집합) : 두 사건 A,B의 공통 부분이 발생하는 사건
  - 합사건(합집합) : 두 사건 A,B 중 적어도 하나가 발생하는 사건
  - 여사건(여집합) : 어떤 사건 A가 발생하지 않는 사건
- 조건부 확률(conditional probability)
  - 사건 A가 발생한 조건 하에 사건 B가 발생할 확률
  - P(B|A) = P(A∩B) / P(A)
- 곱사건과 조건부 확률
  - P(A∩B) = P(A,B) = P(A)P(B|A)
- 독립사건
  - P(A∩B) = P(A)P(B)
- 체인법칙
  - P(A, B, C) = P(A,B)P(C|A,B) = P(A)P(B|A)P(C|A,B)
- P(A) = P(A,B) + P(A,B^C)
  - B와B^C는 서로 배반이고 B∪B^C는 표본공간이됨
  - P(A) = P(A∩S) = P(A∩(B∪B^C)) = P((A∩B)∪(A∩B^C)) = P(A∩B)+P(A∩B^C) = P(A,B) + P(A,B^C)
- P(A) = P(A,B1) + P(A,B2) + P(A,B3) + ... + P(A,Bn)
  - 조건 : 서로 배반인 n개의 사건들의 합집합 B1∪B2∪B3∪... ∪Bn이 표본공간이됨
