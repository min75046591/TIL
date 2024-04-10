# 목차

1. Managing Tables
    - Create a table

    - Modifying table fields

    - Delete a table

2. Modifying Data

    - Insert data

    - Update data

    - Delete data

3. Multi table queries

    - Join

    - Joining tables

&nbsp;

-- limit 은 몇개 offset은 건너뛰는 개수

## 1. Managing Tables

### CREATE TABLE

필드 이름, 데이터 타입, 제약조건

![alt text](image-47.png)
![alt text](image-48.png)

### PRAGMA

![alt text](image-49.png)

### SQLite 데이터 타입

![alt text](image-50.png)

### 제약 조건 - Constraints

- 테이블의 필드에 적용되는 규칙 또는 제한 사항
  - 데이터의 무결성을 유지하고 데이터베이스의 일관성을 보장

![alt text](image-51.png)

<br>

![alt text](image-52.png)

- 자동으로 고유한 정수 값을 생성하고 할당하는 필드 속성

![alt text](image-55.png)

<br>

![alt text](image-54.png)

### SQLite 데이터 타입

![alt text](image-53.png)

&nbsp;

### ALTER TABLE

- 테이블 및 필드 조작

![alt text](image-56.png)

### ALTER TABLE ADD COLUMN syntax

![alt text](image-57.png)

![alt text](image-58.png)

![alt text](image-59.png)
![alt text](image-60.png)
![alt text](image-61.png)

![alt text](image-62.png)
![alt text](image-63.png)

&nbsp;

## 1-3. Delete a table

### DROP TABLE

- 테이블 삭제
![alt text](image-64.png)

&nbsp;

### 참고 - SQLite 타입 선호도의 목적

![alt text](image-66.png)

- 저장하려고 한 데이터에 따라 행이 저장된 data type 다르게 갖음 -> 동적 선호도

![alt text](image-65.png)

&nbsp;

## 2. Modifying Data

![alt text](image-67.png)

## 2-1. Insert data

### INSERT

- 테이블 레코드 삽입

![alt text](image-68.png)
![alt text](image-69.png)
![alt text](image-70.png)
![alt text](image-71.png)

&nbsp;

## 2-2. Update data

### UPDATE

- 테이블 레코드 수정

![alt text](image-72.png)
![alt text](image-73.png)
![alt text](image-74.png)

&nbsp;

## 2-3. Delete data

### DELETE

- 테이블 레코드 삭제

![alt text](image-75.png)
![alt text](image-76.png)
![alt text](image-77.png)

&nbsp;

### 참고

![alt text](image-78.png)

&nbsp;

## 3. Multi table queries

## 3-1. Join

### 관계 : 여러 테이블 간의 (논리적) 연결

![alt text](image-79.png)
![alt text](image-80.png)
![alt text](image-81.png)

<br>

![alt text](image-82.png)

&nbsp;

## 3-2. Joining tables

### JOIN

- 둘 이상의 테이블에서 데이터를 검색하는 방법

- 종류
- 1. INNER JOIN
  - 두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환
  - 교집합!

![alt text](image-83.png)
![alt text](image-84.png)
![alt text](image-85.png)

    - 2. LEFT JOIN
      - 오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환

![alt text](image-86.png)
![alt text](image-87.png)
![alt text](image-88.png)
![alt text](image-89.png)


&nbsp;


### 외래키(Foreign key)

- 의존성을 생성한다.

## 예시 코드

- 외래키 == 제약조건 ->
  - 참조하는 테이블에 미리 생성된 행을 반드시 참조해야한다.
  - 참조하는 외래키 값이 반드시 존재해야하는 제약이 따른다.

- users 테이블

```sql
CREATE TABLE Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30) NOT NULL
);
```

<br>

- 주문 테이블

```sql
CREATE TABLE Orders(
    OrderId INTEGER PRIMARY KEY AUTOINCREMENT,
    OrderDate DATE NOT NULL,
    UserId INTEGER,
    FOREIGN KEY (UserId) REFERENCEs Users(id)
);
```

- 이 내용은 참조무결성에 대해 찾아보면 더 자세히 알 수 있음

![alt text](image-11.png)