# 변수 사용법
# 파이썬

# 서버로부터 데이터를 가져와보세요
# https://fakestoreapi.com/carts

# 너무 어려우니 우리는 남들이 만들어놓은 코드를 가져다가 쓰자!
# -> 라이브러리
# 데이터를 가져오는 python 라이브러리 : requests
# 파이썬 패키지 관리 : pip
    # 설치 : pip install <패키지이름>
    # 목록 확인 : pip list


# 내 코드에 다른 패키지를 추가
import requests
import pprint

api_key = 'f4e4af0f8dab965443dd967405bcb6e9'
# 서울의 위도
lat = 37.56
# 서울의 경도
lon = 126.97


url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
# data = requests.get(url).json()
data = requests.get(url).json()
# 날씨 요약 정보: 서울 기준 'clear sky'가 출력되도록 해보자
pprint.pprint(data['weather'][0]['description'])

# 그냥 출력하기
# print(data)

# 예쁘게 출력하기
pprint.pprint(data)


# 추가 공부 과제
# data['weather']
# data.get('weather')