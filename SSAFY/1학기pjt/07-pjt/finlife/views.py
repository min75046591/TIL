from itertools import product
from django.db.migrations import serializer
from django.http import JsonResponse
import requests
from django.shortcuts import render
from django.conf import settings
from .serializers import DepositProductsSerializer, DepositOptionsSerializer
from .models import DepositOptions, DepositProducts
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# 0. '.env'에 있는 API_KEY 가져오기
api_key = settings.FINLIFE_API_KEY

# Create your views here.
# A. 정기예금 상품 목록 및 옵션 목록 저장
#    - 정기예금 상품 목록을 받아와 DB에 저장할 수 있도록 코드 구현
#    - 단, 비어있는 값에는 -1로 저장해주어야 함

def index(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    
    # 2. JOSN 형식으로 바꿔서 resoponse에 넣어줌
    response = requests.get(url).json()
    
    return JsonResponse(response, safe=False)


def save_deposit_products(request):
    
    # 1. API 가져오는 URL 작성
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    
    # 2. JOSN 형식으로 바꿔서 resoponse에 넣어줌
    response = requests.get(url).json()
    baseListresponse = response['result']['baseList']
    optionListresponse = response['result']['optionList']
    
    
    for li in baseListresponse:
        fin_prdt_cd = li.get('fin_prdt_cd')
        kor_co_nm = li.get('kor_co_nm')
        fin_prdt_nm = li.get('fin_prdt_nm')
        etc_note = li.get('etc_note')
        join_deny = li.get('join_deny')
        join_member = li.get('join_member')
        join_way = li.get('join_way')
        spcl_cnd = li.get('spcl_cnd')

        save_deposit_products = {
            'fin_prdt_cd':fin_prdt_cd,
            'kor_co_nm':kor_co_nm,
            'fin_prdt_nm':fin_prdt_nm,
            'etc_note':etc_note,
            'join_deny':join_deny,
            'join_member':join_member,
            'join_way':join_way,
            'spcl_cnd':spcl_cnd
        }
        

        serializer = DepositProductsSerializer(data=save_deposit_products)
    
        # 유효성 검사
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
    for li in optionListresponse:
        fin_prdt_cd = li.get('fin_prdt_cd')
        intr_rate_type_nm = li.get('intr_rate_type_nm')
        intr_rate = li.get('intr_rate')
        intr_rate2 = li.get('intr_rate2')
        save_trm = li.get('save_trm')
        
        save_deposit_products = {
            'fin_prdt_cd':fin_prdt_cd,
            'intr_rate_type_nm':intr_rate_type_nm,
            'intr_rate':intr_rate,
            'intr_rate2':intr_rate2,
            'save_trm':save_trm,
        }
        print(DepositProducts.objects.filter(fin_prdt_cd = save_deposit_products['fin_prdt_cd']).query)
        for product in DepositProducts.objects.filter(fin_prdt_cd = save_deposit_products['fin_prdt_cd']):
            save_deposit_products['product'] = product.pk

            serializer = DepositOptionsSerializer(data=save_deposit_products)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            
            break
                    
                    
    return JsonResponse({ 'message':'save-good!' })


@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        db = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(db, many=True)
        return Response(serializer.data)
        
    elif request.method == 'POST':    
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def deposit_products_options(request, fin_prdt_cd):
    if request.method == 'GET':
        db = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
        serializer = DepositOptionsSerializer(db, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def top_rate(request):
    if request.method == 'GET':
        # db = DepositOptions.objects.all()
        
        max_rate_product = DepositOptions.objects.prefetch_related('product').order_by('-intr_rate2')[0]
        # prdt_info = DepositProducts.objects.get(fin_prdt_cd=max_rate_product.fin_prdt_cd)
        # print('###############################',max_rate_product.fin_prdt_cd)
        # print(prdt_info)
        serializer = DepositOptionsSerializer(max_rate_product)
        # serializer = DepositProductsSerializer(prdt_info)
        return Response(serializer.data)
        return JsonResponse(safe=fasle)
    
    
    
    '''
    SELECT * FROM DepositOptions
    
    INNER JOIN DepositProducts
    
    ON DepositOptions.product = DepositProducts.fin_prdt_cd;
    
    
    '''