![001](https://github.com/boramH/LC_yeardream9/assets/166669845/c3fe0987-6c9e-4024-803e-5bf743c70f88)
![002](https://github.com/boramH/LC_yeardream9/assets/166669845/8ec0089b-0e1f-41e3-882b-0ea8558a7be6)
<br>
## :scroll: Contents
[1. 프로젝트 소개](#1.-프로젝트-소개)

[2. 프로젝트 진행 순서](#2.-프로젝트-진행-순서)

[3. 결과](#3.-결과)

[4. 프로젝트 회고](#4.-프로젝트-회고)

<br>

## :computer: 프로젝트 소개
### 1) 기획 의도
- 한국의 역사와 문화에 대한 깊이 있는 지식을 제공하여 사용자가 한국사를 보다 쉽고 재미있게 배울 수 있도록 하는 챗봇 개발
- 다양한 역사적 사건, 인물, 문화적 특성에 관한 질문에 실시간으로 응답함으로써 교육적 가치를 높이는 인터랙티브 학습 도구 제작
- 한국사에 대한 광범위한 정보를 데이터베이스로 구축하여 사용자의 질문에 정확하고 상세한 정보를 제공하는 스마트 챗봇 개발
<br>
### 2) 목표
- 지식 기반 구축: LangChain을 사용하여 한국사에 관한 방대한 지식 데이터베이스를 구축하고, 이를 바탕으로 정확한 정보 제공과 깊이 있는 해석을 가능하게 하는 Q&A 엔진을 개발 함. 이를 통해 한국의 역사적 사건, 인물, 문화 등에 대해 질문할 때 신속하고 정확한 답변을 얻을 수 있고자 함.
- 데이터 검증 및 향상: RAG 기술을 이용하여 기존 대규모 언어 모델(Large Language Model, LLM)의 환각(hallucination) 문제를 완화함. 모델이 생성한 내용이 검증된 데이터에 기반하도록 하여 오류를 줄이고, 보다 신뢰할 수 있는 정보 제공이 가능하도록 구현하고자 함.
- 사용자 경험 강화 및 교육적 가치 제공: 한국사에 대한 광범위한 질문에 대해 효과적으로 응답함으로써 사용자 경험을 개선함. 또한, 상호작용을 통해 학습하는 방식으로 교육적 가치를 높이며, 사용자가 역사에 보다 깊이 몰입할 수 있도록 지원하고자 함.

<br>

### 3) 팀원 소개
:crown:임성준(조장)  |  :construction_worker:이우창  |  :information_desk_person:정지석  |  :ok_woman:한보람  |  :raising_hand:신종현  

<br>

### 4) 수행 기간
- 2024.4.17(수) ~ 19(금)

<br>

### 5) 개발 환경
- 개발 언어: Python
- API: gemini-pro
- Vector-store: ChromaDB
- Embedding: models/embedding-001

<br>

## :bulb: 프로젝트 진행 순서
![003](https://github.com/boramH/LC_yeardream9/assets/166669845/04bebe5c-c584-4fcb-8d65-2fe3f682ffae)
<br>

### 1) Deta 수집

- Wikipedia에서 한국사 데이터 수집
- 수집된 데이터를 crawler.py 이용하여 리스트로 저장

- 세부 정보 및 연계 데이터의 수집과 통합: Wikipedia에서 수집된 기본적인 한국사 데이터 수집
- crawler.py 스크립트를 수정하여 추가 데이터 포맷에 맞춰 리스트로 저장하고, 기존의 데이터 구조에 통합하는 작업을 수행

<br>

### 2) 벡터스토어에 저장 및 데이터 검색

- 한국사 데이터 받아 split 후 벡터스토어에 저장, 벡터스토어에서 사용자 입력과 관련된 데이터를 검색을 retriever.py를 이용
![ret](https://github.com/boramH/LC_yeardream9/assets/166669845/f8cb447e-19fd-41b5-8cc1-ace2a5c0efd3)
<br>

### 3) 모델 구축
- Gemini API를 호출하고 user input과 LLM 이용하여 response 도출하는 모델을 gemini.py를 이용하여 구축
![model](https://github.com/boramH/LC_yeardream9/assets/166669845/8c92ad50-1e97-4952-bf37-2442713bf878)
<br>

### 5) 로그 기록
- 사용자 입력, 모델, 체인 작동 내역을 logger.py를 이용하여 기록
- 로그 시간 출력, 체인 기능이 동작되는 시간 및 모델이 답변하는 시간 구현
![lang](https://github.com/boramH/LC_yeardream9/assets/166669845/fa25e71b-6e6e-4f23-9458-78c8363280aa)

<br>


## :trophy: 3.결과
- main.py로 전체 모듈 최종 구현

![model](https://github.com/boramH/LC_yeardream9/assets/166669845/8c92ad50-1e97-4952-bf37-2442713bf878)

<br>

## :pencil: 4. 프로젝트 회고

### 발전 방향
1) pdf 자료로 데이터 수집 시도 후 CSV 자료로 변경
2) 네이버 지식백과를 데이터로 사용했으나 관련 없는 데이터가 수집되어 위키백과로 데이터 수집처 변경
3) Db 출처 확인 기능 구현을 랭체인 공식문서를 참고하여 반영함
4) VectorDB 저장을 피클 구현했으나 persist_directory="./data.db" 으로 변경

### 회고
1) 크롤링 단계에서 스플릿 모듈과 인베딩 모듈을 다른 모듈로 사용하면 더 좋은 결과를 도출할 수 있었을 것으로 예상됨
2) 팀원 간의 협력과 깃허브를 배우고 경험 할 수 있는 좋은 기회가 되었고, 협업 능력이 향상 됨
3) 해당 기술을 통해 더 다양한 프로젝트를 구현할 수 있을 것으로 예상 됨




