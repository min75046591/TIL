# 목차

1. Database

2. Realational Database

3. SQL

4. Single Table Queries
    - Querying data

    - Sorting data

    - Filtering data

    - Grouping data

## 1. Database

- 체계적인 데이터 모음

### 데이터

- 저장이나 처리에 효율적인 형태로 변환된 정보

<br>

데이터 사용량이 증가하고 데이터 센터의 성장에 따라  
**데이터를 저장하고 잘 관리하여 활용할 수 있는 기술이 중요해짐**

<br>

### 기존의 데이터 저장 방식

1. 파일(File) 이용

   - 어디에서나 쉽게 사용 가능

   - 데이터를 구조적으로 관리하기 어려움

<br>

![alt text](image.png)

1. 스프레드 시트(Spreadsheet) 이용

    - 테이블의 열과 행을 사용해 데이터를 구조적으로 관리 가능
![alt text](image-1.png)

- 스프레드 시트의 한계
  - 크기 : 일반적으로 약 100만 행까지만 저장 가능
  
  - 보안 : 단순히 파일이나 링크 소유 여부에 따른 단순한 접근 권한 기능 제공

  - 정확성
  ![alt text](image-2.png)

<br>

### 데이터베이스 역할

- 데이터를 저장하고 조작 = CRUD

&nbsp;

## 2. Realational Database

![alt text](image-3.png)

### 관계형 데이터베이스

- 데이터 간에 **관계**가 있는 데이터 항목들의 모음

  - 관계 : 여러 테이블 간의 (논리적) 연결

![alt text](image-4.png)

<br>

![alt text](image-5.png)

- 고객 데이터 간 비교를 위해서는 각 데이터에 고유한 식별 값을 부여한다.

  - 기본 키(id), Primary Key

<br>

- 누가 어떤 주문을 했는지 어떻게 식별?

  - 외래 키, Foreign Key(고객 ID)
  
<br>

![alt text](image-6.png)

<br>

### 관계형 데이터베이스 관련 키워드

1. Table (aka Realation)
    - 데이터를 기록하는 곳

2. Field (aka Column, Attribute)
    - 각 필드에는 고유한 데이터 형식(타입)이 지정됨

3. Record (aka Row, Tuple)
   - 각 레코드에는 구체적인 데이터 값이 저장됨

4. Database
    - 테이블의 집합

5. Primary Key (기본 키, PK)
    - 각 레코드의 고유한 값
    - 관계형 데이터베이스에서 **레코드의 식별자**로 활용

6. Foreign Key (외래 키, FK)
    - 테이블의 필드 중 다른 테이블의 레코드를 식별할 수 있는 키
    - 다른 테이블의 기본 키를 참조
    - 각 레코드에서 서로 다른 테이블 간의 **관계를 만드는데** 사용

&nbsp;

## RDBMS

### DBMS - Database Management System : 데이터베이스를 관리하는 소프트웨어 프로그램

- 데이터 저장 및 관리를 용이하게 하는 시스템

- 데이터베이스와 사용자 간의 인터페이스 역할

- 사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구 등을 할 수 있도록 도움

<br>

### RDBMS - Relational Database Management System

- 관계형 데이터베이스를 관리하는 소프트웨어 프로그램

  - RDMBS 서비스 종류 : SQLite, MySQL, Oracle Database 등

### SQLite

- 경량의 오픈 소스 데이터베이스 관리 시스템
  - 컴퓨터나 모바일 기기에 내장되어 간단하고 효율적인 데이터 저장 및 관리를 제공

<br>

### 데이터베이스 정리

- Table은 데이터가 기록되는 곳

- Table에는 행에서 고유하게 식별 가능한 기본 키(PK) 라는 속성이 있으며, 외래 키를 사용하여 각 행에서 서로 다른 테이블간의 관계를 만들 수 있다!

- 데이터는 기본 키 또는 외래 키를 통해 결합(join)될 수 있는 여러 테이블에 걸쳐 구조화됨

&nbsp;

## 3. SQL - Structure Query Language

![alt text](image-10.png)


<br>


### SQL Syntax

~~~~sql
SELECT colums_name FROM table_name;
~~~~

- 1. SQL 키워드는 대소문자를 구분하지 않음
    - BUT!! 대문자로 작성하는 것을 권장 (명시적 구분)

- 2. 각 SQL Statements의 끝에는 세미콜론(';') 이 필요
    - 세미콜론은 각 SQL Statements를 구분하는 방법 (명령어의 마침표)


<br>


### SQL Statements

- SQL을 구성하는 가장 기본적인 코드 블록

![alt text](image-12.png)

![alt text](image-13.png)

![alt text](image-7.png)

- DCL은 잘 사용하지 않고 DQL(데이터 검색)이 가장 중요!!

<br>

#### 단순히 SQL 문법을 암기하고 상황에 따라 실행만 하는 것이 아닌 SQL을 통해 관계형 데이터베이스를 잘 이해하고 다루는 방법을 학습

<br>

### 참고 - Query

- 데이터베이스로부터 정보를 요청 하는 것

- 일반적으로 SQL로 작성하는 코드를 쿼리문(SQL문)이라 함


&nbsp;


## 4. Single Table Queries

### SQL Statements 유형

![alt text](image-8.png)

## 4-1. Querying data

### 1. SELECT

- **SELECT** statement
    - 테이블에서 데이터를 조회

    - 테이블의 필드를 정하는 일

![alt text](image-9.png)
![alt text](image-14.png)
![alt text](image-15.png)
![alt text](image-16.png)

### SELECT 정리
  
  - 테이블의 데이터를 조회 및 반환

  - '*' (asterisk)를 사용하여 모든 필드 선택


&nbsp;


## 4-2. Sorting data - ORDER BY

- 조회 결과의 레코드를 정렬

![alt text](image-17.png)
![alt text](image-18.png)
![alt text](image-19.png)
![alt text](image-20.png)
![alt text](image-21.png)
![alt text](image-22.png)


&nbsp;


## 4-3. Filtering data

![alt text](image-23.png)

<br>

### DISTINCT

- 조회 결과에서 **중복**된 레코드를 제거

![alt text](image-24.png)

<br>

### WHERE

- 조회 시 특정 검색 조건을 지정
![alt text](image-25.png)
![alt text](image-26.png)
![alt text](image-27.png)
![alt text](image-28.png)
![alt text](image-29.png)
![alt text](image-30.png)
![alt text](image-31.png)
![alt text](image-32.png)
![alt text](image-33.png)
![alt text](image-34.png)


&nbsp;


### Operators

![alt text](image-35.png)

![alt text](image-36.png)

### IN : 값이 특정 목록 안에 있는지 확인

### LIKE : 값이 특정 패턴에 일치하는지 확인 (Wildcards와 함께 사용)

![alt text](image-37.png)

### LIMIT : 조회하는 레코드 수를 제한

![alt text](image-38.png)
![alt text](image-39.png)

- LIMIT 하나만 적으면 몇개를 뽑을지

- 2개 적으면 위에 몇개 건너뛰고 몇개를 조회할지 -> 즉 offset은 첫번째 숫자 2번째 숫자는 limit

![alt text](image-40.png)

&nbsp;

### GROUP BY

- 레코드를 그룹화하여 요약본 생성 ('집계 함수'와 함께 사용)

### Aggregation Functions : 집계 함수

- 값에 대한 계산을 수행하고 단일한 값을 반환하는 함수 -> SELECT 안에 사용

- SUM, AVG, MAX, MIN, COUNT

![alt text](image-41.png)
![alt text](image-42.png)
![alt text](image-43.png)

<br>

![alt text](image-44.png)
![alt text](image-45.png)

<br>

![alt text](image-46.png)