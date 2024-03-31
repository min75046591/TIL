# 목차

1. Web Application

    - 클라이언트와 서버

    - Frontend & Backend

<br/>

2. Framework
    - Web Framework

    - Django Framework

    - 가상 환경

    - Django 프로젝트

<br/>

3. Django Design Pattern
    - Project & App

    - 요청과 응답

&nbsp;

# 1. Web Application

- 웹 어플리케이션 개발 : 인터넷을 통해 사용자에게 제공되는 소프트웨어 프로그램을 구축하는 과정.
  - 다양한 디바이스(모바일, 태블릿, PC 등)에서 웹 브라우저를 통해 접근하고 사용할 수 있음

## 1-1. 클라이언트와 서버

### 웹의 동작 방식

- Client : 서비스를 요청하는 주체 (웹 사용자의 인터넷이 연결된 장치, 웹 브라우저)

- Server : 클라이언트의 요청에 응답하는 주체 (웹 페이지, 앱을 저장하는 컴퓨터)

<br/>

## 1-2. Frontend & Backend

### Frontend (프론트엔드)

- 사용자 인터페이스(UI)를 구성하고, 사용자가 애플리케이션과 상호작용을 할 수 있도록 함
-> HTML, CSS, JavaScript, 프론트엔드 프레임워크 등

### Backend(백엔드)

- 서버 측에서 동작하며, 클라이언트의 요청에 대한 처리와 데이터베이스와의 상호작용 등을 담당
-> 서버 언어(Python, Java 등) 및 백엔드 프레임워크, 데이터베이스, API, 보안 등

<br/>

# 2. Framework

## 2-1. Web Framework
>
> 웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구 (개발에 필요한 기본 구조, 규칙, 라이브러리 등)

<br/>

## 2-2. Django Framework

### django
>
> Python 기반의 대표적인 웹 프레임워크

- 다양성, 확장성, 보안, 커뮤니티 지원 등의 장점이 있음

<br/>

## 2-3. 가상 환경
>
> Python 애플리케이션과 그에 따른 패키지들을 격리하여 관리할 수 있는 **'독립적인'** 실행 환경

-필요한 이유 : 한 개발자가 2개의 프로젝트를 진행한다고 할 때, 각각 다른 버전이 필요하지만
            파이썬 환경에서 패키지는 1개의 버전만 존재할 수 있음. 따라서 각각 다른 패키지
            버전 사용을 위해 **독립적인 개발 환경**이 필요함

### 가상 환경 venv 생성
>
> git bash 명령어: python -m venv venv  (virtual environment)

### 가상 환경 활성화
>
> $ source venv/Scripts/activate

### 패키지 목록이 필요한 이유
>
> 여러명의 개발자가 하나의 프로젝트를 함께 개발할 때 다른 팀원이 프로젝트를 위해 어떤 패키지를 설치했고, 어떤 버전을 설치했는지의 가상 환경 상황을 알기 위해. 즉, **가상 환경에 대한 정보 즉 패키지 목록이 공유되어야함.**

- 의존성 패키지 : 한 소프트웨어 패키지가 다른 패키지의 기능이나 코드를 사용하기 때문에 그 패키지가 존재해야만 제대로 작동하는 관계. 없거나 버전이 다르면 오류나 예상치 못한 동작을 보일 수 있음.

### 의존성 패키지
>
> 목록 생성 : pip freeze > requirements.txt
<br/>
> 의존성 패키지 관리의 중요성 : 개발 환경에서는 각각의 프로젝트가 사용하는 패키지와 그 버전을 정확히 관리하는 것이 중요!
   -> 가상 환경 & 의존성 패키지 관리

<br/>

## 2-4. Django 프로젝트

### Django 프로젝트 생성 전 루틴

1. 가상환경 생성

- $ python -m venv venv

2. 가상환경 활성화

- $ source venv/Scripts/activate

3. Django 설치

- $ pip install django

4. 의존성 파일 생성 (패키지 설치시마다 진행)

- $ pip freeze > requirements.txt

5. Django 프로젝트 생성

- $ django-admin startproject (프로젝트이름) .

6. Django 서버 실행

- $ python manage.py runserver

<br/>

### Django 프로젝트 생성 루틴 정리 + git

~~~~
1. 가상 환경 생성

2. 가상 환경 활성화

3. Django 설치

4. 의존성 파일 생성 (requirements.txt) -> 패키지 설치시마다 진행

5. .gitignore 파일 생성 (첫 add 전)

6. git 저장소 생성

7. Django 프로젝트 생성
~~~~

<br>

### 가상 환경을 사용하는 이유

- 의존성 관리
  - 라이브러리 및 패키지를 각 프로젝트마다 독립적으로 사용 가능

- 팀 프로젝트 협업
  - 모든 팀원이 동일한 환경과 의존성 위에서 작업하여 버전간 충돌 방지!

<br/>

### LTS (Long-Term-Support)

- 프레임워크나 라이브러리 등의 소프트웨어에서 장기간 지원되는 안정적인 버전을 의미할 때 사용

- 기업이나 대규모 프로젝트에서는 소프트웨어 업그레이드에 많은 비용과 시간이 필요하기 때문에 안정적이고 장기간 지원되는 버전이 필요

<br/>

장고는 풀스택 프레임워크 이지만, 장고가 제공하는 프론트엔드 기능은 다른 전문적인 프론트엔드 프레임워크들에 비해 매우 미흡함. 따라서 엄밀히 말하면 풀스택 영역에서 백엔드에 속한다고 볼 수 있음. 그래서 풀스택 혹은 백엔드 프레임워크라 부름

&nbsp;

# 3. Django Design Pattern

### 디자인 패턴
>
> 소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책 (공통적인 문제를 해결하는 데 쓰이는 형식화 된 관행)

> **"애플리케이션의 구조는 이렇게 구성하자!"** 라는 관행

<br/>

#### MVC 디자인 패턴 (Model, View, Controller)
>
> 애플리케이션을 구조화하는 대표적인 패턴 (데이터 & 사용자 인터페이스 & 비즈니스 로직을 분리)

> 시작적 요소와 뒤에서 실행되는 로직을 서로 영향없이, 독립적이고 쉽게 유지 보수할 수 있는 애플리케이션을 만들기 위해

<br>

#### MTV 디자인 패턴 (Model, Template, View)
>
> Django 에서 애플리케이션을 구조화하는 패턴 (기존 MVC 패턴과 동일하나 단순히 명칭을 다르게 정의한 것)

> 다 앱에 존재해야함!

<br/>

## 3-1. Project & App

### Django project
>
> 애플리케이션의 집합 (DB 설정, URL 연결, 전체 앱 설정 등을 처리)

### Django application
>
> 독립적으로 작동하는 기능 단위 모듈 (각자 특정한 기능을 담당. 다른 앱들과 함께 하나의 프로젝트를 구성)

<br>

### 앱을 사용하기 위한 순서

#### 1. 앱 생성

: python manage.py startapp articles

#### 2. 앱 등록

: firstpjt -> settings -> 앱 등록 'articles'

### 프로젝트 구조

- settings.py
  - 프로젝트의 모든 설정을 관리

- urls.py
  - 요청 들어오는 URL에 따라 이에 해당하는 적절한 views를 연결

- **init**.py
    -

### 요청과 응답

- views.py 가 가장 많은 역할을 함과 동시에 중요!

> view 함수 사용

> 1, 2, 3, 4 순서도 머리에 잘 넣기!

-----

장고 루틴

1. 가상환경 생성 (venv란? virtual environment 의 약자로 가상환경을 뜻함)
python -m venv venv

>> {python파일을} {만든다} {가상환경을} {이름은 venv로}

2. 가상환경 활성화
source venv/Scripts/activate

>> source 명령어는 스크립트 파일을 수정한 후에 수정된 값을 바로 적용하기 위해 사용. (리부팅 없이 즉시 적용하기 위해 사용)

3. Django 설치
pip install django

>> 여기서 pip이란 package installer of python으로 파이썬 패키지나 모듈의 패키지 매니저이다.

4. 의존성 파일 생성
pip freeze > requirements.txt

>> pip freeze 명령어는 현재 작업 환경(가상 환경)에 설치되어있는 패키지의 리스트들을 모두 출력해준다
여기서 > requirements.txt 를 해주면 requirements.txt파일에 출력한 리스트들을 모두 저장해준다.
=====================

- Django 프로젝트 생성
django-admin startproject firstpjt .

>>firstpjt라는 이름의 프로젝트를 생성해준다.

- Django 서버 실행
python manage.py runserver

>>{python파일}인 {manage.py}를 실행시켜서 {서버를실행한다}
>>manage.py와 동일한 경로에서 진행해주어야 한다.

-git에 올릴거면 (첫 add 전) .gitignore파일을 만들어서 gitignore.io 에 들어가서 내용을 입력해준다.
그 이후 git 저장소 생성해준뒤 Django 프로젝트를 생성해준다.
