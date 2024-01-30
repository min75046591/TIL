import requests
from pprint import pprint


URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'
params = {
    'ttbkey': 'ttbch050361148001',
    'Query' : 'title',
    'QueryType': 'Title',
    'MaxResults': 20,
    'start': 1,
    'SearchTarget': 'Book',
    'output': 'js',
    'Version': '20131101',
}  


def get_author(book_title):
    
    # URL에서 필요한 정보 가져와라
    response_author = requests.get(URL, params=params).json()
    pprint(response_author)
    response_author['item'] 
    # 작가의 각 책에 대한 정보 추출
    # books = response_json_author.get('item', [])





# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_author('베니스의 상인'))

    # pprint(get_author('개미'))

    # pprint(get_author('*'))
