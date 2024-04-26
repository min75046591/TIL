from urllib import response
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
import requests
from django.conf import settings


# Create your views here.


# A. 서울의 5일 치 예보 데이터 확인
def index(request):
    api_key = settings.WEATHER_API_KEY
    city_name = 'Seoul,KR'
    
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'
    response = requests.get(url).json()
    return JsonResponse(response)


# B. 원하는 데이터만 DB에 저장
def save_data(request):
    api_key = settings.WEATHER_API_KEY
    city_name = 'Seoul,KR'
    
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}'
    response = requests.get(url).json()
    
    for li in response.get('list'):
        # 원하는 데이터 추출하기
        dt_txt = li.get('dt_txt')
        temp = li.get('main').get('temp')
        feels_like = li.get('main').get('feels_like')
        
        print('dt_txt = ', dt_txt)
        print('temp = ', temp)
        print('feels_like = ', feels_like)
        
        "민수야"
        " 그만 자고 "
        "열심히 해야지? "
        " 노래 플레이리스트 알아서 들어와 "
        " 알 겠 냐 ? "
        
        
        
        