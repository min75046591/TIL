# 1. Template System


<br/>

### requirements 파일 다운받는 방법
~~~~
    pip install -r requirements.txt
~~~~

# 2. 템플릿 상속

### 템플릿 상속 - Template inheritance
> **페이지의 공통요소를 포함** 하고, **하위 템플릿이 재정의 할 수 있는 공간** 을 정의하는 기본 스켈레톤 템플릿을 작성하여 상속 구조를 구축


### 'extend' **tag**



### 'block' **tag**

하위 템플릿에서 재정의 할 수 있는 블록을 정의

이름이 필요


# 3. HTML form (요청과 응답)


### 데이터를 보내고 가져오기

> HTML 'form' element를 통해 사용자와 애플리케이션 간의 상호작용 이해하기

url 이나 form을 통해 서버에 요청을 보낼 수 있음


get -> url 노출
post -> 로그인에서 많이 사용 -> 인증에서 사용됨

### 'input' element

> 사용자의 데이터를 입력 받을 수 있는 데이터

### 'name' attribute -> input의 핵심 속성

> 입력한 데이터에 붙이는 이름(key)

- 문자열은 앰퍼샌드 ('&')로 연결된 key=value 쌍으로 구성

- 기본 url 과는 ('?')로 구분 됨 


### BASE_DIR

'C://desktop/ssafy/aaaa/aaaa/....  -> 리눅스 계열의 OS

'C:\\desktop\\ -> 윈도우에서의 경로 표기

> OS 마다 객체 지향 파일 시스템 경로가 다르다!

### DTL 주의사항

- Python처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만 명칭을 그렇게 설계 했을 뿐, **Python 코드로 실행되는 것이 아니며 Python과는 관련 없음**

- 프로그래밍적 로직이 아니라 표현을 위한 것임을 명심!

- 프로그래밍적 로직은 되도록 view 함수에서 작성 및 처리할 것

- 공식문서를 참고해 다양한 태그와 필터 사용해보기