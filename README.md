# Django ERD



## I. 프로젝트 목표

- 사용자에게 영화 목록을 알려주고, 영화 세부정보 출력
  - 영화 세부정보마다 영화 데이터를 수정, 삭제하는 기능 구현
- 영화 세부정보에 사용자가 직접 comment를 추가할 수 있는 기능 구현
- Database 관계를 이해하고 다수의 테이블간 관계를 정의하여 서비스 구현





## II. 개발 환경

- IDE: PyCharm
- 서버: python(3.7.2)
- 프론트엔드: html/css
- 웹 프레임워크: django
- ORM: django orm
- Database: sqlite3



## III. 데이터 모델링

### (1) Genre

- 영화의 장르 정보가 담긴 테이블
- Movie내 레코드와 1:N 관계 형성



### (2) Movie

- 영화의 상세 정보가 담긴 테이블
- genre 속성은 Genre 테이블의 id를 왜래키로 받아 정보를 출력
- Score내 레코드와 1:N 관계 형성



### (3) Score

- 사용자가 등록한 comment의 정보
- 하나의 Movie 레코드와 1:N 관계 형성
- Movie 테이블의 id를 왜래키로 받아 연결





## III. 구현 기능

### (1) 영화 리스트

- '/movies/' url 주소에서 모든 영화의 포스터와 제목 표시
- html 문서 내 grid 방식으로 영화 정보 출력
- 영화 제목을 클릭하면 영화 상세정보 페이지로 이동



### (2) 영화 상세 정보

- '/movie/'에 영화의 id를 추가해 url 구성
- 해당 영화의 모든 정보를 출력하고 수정, 삭제 기능을 button으로 구현
- 영화의 장르는 Genre 테이블의 해당하는 장르를 출력



### (3) 영화 한줄평

- 영화 상세정보 페이지 하단에 사용자가 등록한 comment 출력
- form 태그를 통해 영화 평점과 한줄평을 등록
- Movie에 등록된 모든 comment를 출력