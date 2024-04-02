-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');

-- 테이블 만들기
CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    content VARCHAR(200) NOT NULL,
    createdAt DATE Not Null
);

-- 테이블 확인
PRAGMA table_info('articles');



-- 1. Insert data into table
INSERT INTO articles (title, content, createdAt)
VALUES 

('title4', 'world4', DATE());


SELECT * FROM articles;



-- 2. Update data in table
UPDATE
  articles
SET
  title = 'Update Title'
WHERE
  id = 1;

SELECT * FROM articles;

-- 한번에 두개도 바꿀 수 있다
UPDATE
  articles
SET
  title = 'Update Title',
  content = 'update content'
WHERE
  id = 2;



-- 3. Delete data from table
DELETE FROM articles
WHERE
    id = 6;

-- 없는걸 확인 가능. 하지만 에러를 발생시키진 않음
SELECT * FROM articles WHERE id = 6;

-- sub query
DELETE FROM
    articles
WHERE id IN (
    SELECT id FROM articles
    ORDER BY createdAt 
    LIMIT 2
);

SELECT * FROM articles;