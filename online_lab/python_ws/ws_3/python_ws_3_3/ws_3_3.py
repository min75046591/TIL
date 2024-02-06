# 1682 도서 대여 서비스
def rental_book(name, how_many):
    decrease_book(how_many)
    print('남은 책의 수 :', number_of_book)
    print(f'{name}님이 {how_many}권의 책을 대여하였습니다.')
number_of_book = 100

def decrease_book(how_many):
    global number_of_book
    number_of_book -= how_many

rental_book('홍길동', 3)