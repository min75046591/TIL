# 클래스 정의
class Person:  
    blood_color = 'red'       
               
    def __init__(self, name):
        self.name = name
        
    def singing(self):
        return f'{self.name}가 노래합니다.'





# class는 paskalCase를 사용 -> 대문자 사용 가능
# 그 전에는 snake.case를 사용. 하지만 클래스도 사용은 가능
# But 클래스와 다른걸 구분하기 위해 파스칼케이스를 쓰기로 정함
# ()를 생략 가능. 사용해도 문제는 없음


# 인스턴스 생성 -> 클래스로 만들어진 객체인 인스턴스다
singer1 = Person('iu')
singer2 = Person('bts')

# 메서드 호출
print(singer1.singing())
print(singer2.singing())

# 속성(변수) 접근
print(singer1.blood_color)
print(singer1.blood_color)