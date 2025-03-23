# 라이브러리 : 남들이 만들어놓은 코드를 가져다가 쓰자!
# 데이터를 가져오는 python 라이브러리(패키지) : requests
# 파이썬 패키지 관리 : pip
    # 설치 : pip install <패키지이름>
    # 목록 확인 : pip list

# 내 코드에 다른 패키지를 추가
import requests
import pprint

api_key = '87246d75e1ce26e1392a087b3d1d88c5'
# 서울의 위도
lat = 37.56
# 서울의 경도
lon = 126.97

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
data = requests.get(url).json()

# 그냥 출력하기
# print(data)

# 예쁘게 출력하기
pprint.pprint(data)

# 날씨 요약 정보 : 서울 기준 'clear sky' 가 출력되도록 해보자!
pprint.pprint(data.get('weather')[0].get('description'))

# 추가 공부 과제 두 가지 방식은 모두 정상적으로 동작합니다.
# 차이점이 무엇일까요 ?
# data['weather']
# data.get('weather')


