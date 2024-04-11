# 목차
- 1. REST API
    - 1-1. 자원의 식별
    - 1-2. 자원의 행위
    - 1-3. 자원의 표현

- 2. DRF with Single Model
    - 2-1. DRF
    - 2-2. GET
    - 2-3. POST
    - 2-4. DELETE
    - 2-5. PUT

&nbsp;

## 1. REST API - Application Programming Interface

- 두 소프트웨어가 서로 통신할 수 있게 하는 메커니즘
    - 클라이언트-서버처럼 서로 다른 프로그램에서 요청과 응답을 받을 수 있도록 만든 체계

![Alt text](image.png)
![Alt text](image-1.png)
![Alt text](image-2.png)
![Alt text](image-3.png)
![Alt text](image-4.png)
![Alt text](image-5.png)
![Alt text](image-6.png)

<br>

### REST API

- REST라는 설계 디자인 약속을 지켜 구현한 API

![Alt text](image-7.png)

<br>

### REST에서 자원을 사용하는 법 3가지

- 1. 자원의 "식별"
    - URL

- 2. 자원의 "행위"
    - HTTP Methods

- 3. 자원의 "표현"
    - JSON 데이터
    - 궁극적으로 표현되는 데이터 결과물


&nbsp;


## 1-1. 자원의 식별

- 통합 자원 식별자  

![Alt text](image-8.png)

<br>

- 통합 자원 위치  

![Alt text](image-9.png)
![Alt text](image-10.png)
![Alt text](image-11.png)
![Alt text](image-12.png)
![Alt text](image-13.png)
![Alt text](image-14.png)
![Alt text](image-15.png)
![Alt text](image-16.png)


&nbsp;


## 1-2. 자원의 행위

### HTTP Request Methods

- 리소스에 대한 행위(수행하고자 하는 동작)를 정의
    - HTTP verbs 라고도 함

![Alt text](image-17.png)

<br>

### HTTP response status codes

- 특정 HTTP 요청이 성공적으로 완료 되었는지 여부를 나타냄

![Alt text](image-18.png)

&nbsp;

## 1-3. 자원의 표현

![Alt text](image-19.png)
![Alt text](image-20.png)
![Alt text](image-21.png)
![Alt text](image-22.png)
![Alt text](image-23.png)

<br>

![Alt text](image-24.png)
![Alt text](image-25.png)
![Alt text](image-26.png)


&nbsp;


## 2. DRF with Single Model

## 2-1. DRF

### Django REST framework - DRF

- Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리

### 프로젝트 준비

- 사전 제공된 drf 프로젝트 기반 시작

1. 가상 환경 생성, 활성화 및 패키지 설치

2. migrate 진행

```
$ python manage.py migrate
```

3. 준비된 fixtures 파일을 load하여 실습용 초기 데이터 입력
```
$ python manage.py loaddata articles.json
```

![Alt text](image-27.png)
![Alt text](image-28.png)
![Alt text](image-29.png)
![Alt text](image-30.png)


&nbsp;


## 2-2. GET

![Alt text](image-31.png)

### Serialization - 직렬화

- 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정

- 어떠한 언어나 환경에서도 나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정

![Alt text](image-32.png)
![Alt text](image-33.png)

<br>

![Alt text](image-34.png)

### Serializer

- Serialization을 진행하여 Serialized data를 반환해주는 클래스

### ModelSerializer

- Django 모델과 연결된 Serializer 클래스
    - 일반 Serializer와 달리 사용자 입력 데이터를 받아 자동으로 모델 필드에 맞추어 Serialization을 진행

![Alt text](image-35.png)
![Alt text](image-36.png)
![Alt text](image-37.png)
![Alt text](image-38.png)

### 'api_view' decorator

- DRF view 함수에서는 **필수로 작성**되며 view 함수를 실행하기 전 HTTP 메서드를 확인

- 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는 405 Method Not Allowed로 응답

- DRF view 함수가 응답해야 하는 HTTP 메서드 목록을 작성

<br>

![Alt text](image-39.png)
![Alt text](image-40.png)
![Alt text](image-41.png)


&nbsp;


## 2-3. POST

- 게시글 데이터 생성하기

1. 데이터 생성이 성공했을 경우 201 Created 응답

2. 데이터 생성이 실패 했을 경우 400 Bad request 응답

![Alt text](image-42.png)
![Alt text](image-43.png)
![Alt text](image-44.png)


&nbsp;


## 2-4. DELETE

![Alt text](image-45.png)
![Alt text](image-46.png)


&nbsp;


## 2-5. PUT

![Alt text](image-47.png)
![Alt text](image-48.png)
![Alt text](image-49.png)

<br>

### 'partial' argument

- 부분 업데이트를 허용하기 위한 인자

- 예를 들어 partial 인자 값이 False일 경우 게시글 title 만을 수정하려고 해도 반드시 content 값도 요청 시 함께 전송해야 함

- 기본적으로 serializer는 모든 필수 필드에 대한 값을 전달 받기 때문
    - 즉, 수정하지 않는 다른 필드 데이터도 모두 전송해야 하며 그렇지 않으면 유효성 검사에서 오류가 발생

![Alt text](image-50.png)

&nbsp;

### 참고

![Alt text](image-51.png)