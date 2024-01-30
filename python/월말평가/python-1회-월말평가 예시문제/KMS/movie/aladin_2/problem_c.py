import requests
from pprint import pprint

ttbkey = 'ttbch050361148001'
query_type = 'Author'
max_result = 20
start = 1
search_target = 'Book'
output = 'js'
version = 20131101


URL = f'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&Query=aladdin&QueryType={query_type}&MaxResults={max_result}&start={start}&SearchTarget={search_target}&output={output}&Version={version}'




    # 여기에 코드를 작성합니다.
author_name = '파울로 코엘료'
   
URL_author = f'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx?ttbkey={ttbkey}&Query={author_name}&QueryType={query_type}&MaxResults={max_result}&start={start}&SearchTarget={search_target}&output={output}&Version={version}'
    # URL에서 필요한 정보 가져와라
response_author = requests.get(URL_author)
    # 가져온 정보를 json 형식으로 전환
response_json_author = response_author.json()

    # 작가의 각 책에 대한 정보 추출
books = response_json_author.get('item', [])
    
def bestseller_book():
    
    best_books = []
    for book in sorted(books, key=lambda x: x.get('salesPoint', 0), reverse=True)[:5]:
        best_books.append(book['title'])
        #print(book)
    
    #best_books.get('title')
    return best_books






# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(bestseller_book())
