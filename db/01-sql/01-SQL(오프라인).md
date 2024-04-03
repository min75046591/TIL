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


### PRAGMA

### SQLite 데이터 타입



&nbsp;


## 2. Modifying table fields

### ALTER TABLE ADD COLUMN syntax




### 참고 - SQLite 타입 선호도의 목적
- 저장하려고 한 데이터에 따라 행이 저장된 data type 다르게 갖음 -> 동적 선호도


&nbsp;


## 3. Modifying Data



## 4. Multi table queries

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

<br>

### JOIN clasue
- 둘 이상의 테이블에서 데이터를 검색하는 방법

- 두 종류
    - 1. INNER JOIN

    - 2. LEFT JOIN