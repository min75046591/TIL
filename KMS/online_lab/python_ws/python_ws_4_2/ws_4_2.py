# requests 모듈을 임포트(http요청을 보내기 위한 모듈)
import requests
# pprint 에서 pprint 함수를 print라는 이름으로 임포트 - 서버에서 주는 데이터를 구조화해서 보여주는 모듈
from pprint import pprint as print


# 요청할 API 주소에서 맨 뒤에 변화할 값만 제외하고 변수에 할당한다.
API_URL = 'https://jsonplaceholder.typicode.com/users/'

# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()

# 응답 데이터 출력
# print(response)

# 변환 데이터 출력
# print(parsed_data)

# 변환 데이터의 타입
# print(type(parsed_data))

# 특정 데이터 출력
dummy_data = []


for data in range(len(parsed_data)):
    parsed_data[data]['name']
    dummy_data.append(parsed_data[data]['name'])

print(parsed_data)