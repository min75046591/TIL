# 07-pjt (금융)

## 김민수

- 기본 세팅 (model작성, setting에 앱과 API 세팅, )

- B. 전체 정기예금 상품 목록 출력

- C. 정기예금 상품 추가하기


<br>

### 배운점

1. API를 통해 데이터를 추출하고 serializer로 직렬화 하여 데이터 추출에 대해 배웠습니다.  


2. .env 파일에 API KEY를 넣고 이를 settings에 등록하고, env라는 환경 변수를 설정!

```python
import os
import environ

env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR,'.env')
)

# 금융 API_KEY로 내 API 정리
FINLIFE_API_KEY = env('API_KEY')
```

위 코드는 Python 프로젝트에서 환경 변수를 설정하고 관리하기 위해 사용되는 코드입니다.

import os: 파이썬 내장 모듈인 os를 import하여 운영체제와 상호 작용할 수 있는 기능을 제공합니다.  

import environ: django-environ이라는 외부 패키지를 import합니다. 이 패키지는 환경 변수를 관리하기 위한 편리한 도구를 제공합니다.  

env = environ.Env(DEBUG=(bool, True)): environ.Env 객체를 생성합니다. 이 객체는 환경 변수를 로드하고 사용할 때 필요한 설정을 담고 있습니다. 여기서 DEBUG는 환경 변수의 이름이고, (bool, True)는 해당 변수의 기본값을 지정합니다. 이 경우 DEBUG 변수는 부울 값(True 또는 False)을 가지며 기본값은 True로 설정됩니다.  

environ.Env.read_env(env_file=os.path.join(BASE_DIR,'.env')): .env 파일에서 환경 변수를 읽어옵니다. .env 파일은 프로젝트 루트 디렉토리에 위치하며, 여기에는 프로젝트에 필요한 환경 변수들이 설정되어 있습니다. BASE_DIR은 프로젝트의 루트 디렉토리를 나타내는 변수로, os.path.join(BASE_DIR,'.env')은 .env 파일의 전체 경로를 구성합니다.  

이렇게 설정된 환경 변수들은 프로젝트 전체에서 env 객체를 통해 사용할 수 있으며, 각종 설정 정보나 민감한 정보를 안전하게 관리할 수 있습니다. Django 프로젝트에서는 이 방식을 통해 데이터베이스 연결 정보, 비밀 키 등을 환경 변수로 설정하여 보안을 강화하는 경우가 많습니다.  

<br>

3. serializers.py에서 원하는 부분을 포함하여 넣으려면,

```python
class DepositOptionsSerializer(serializers.ModelSerializer):
    
    product = DepositProductsSerializer()
    class Meta:
        model = DepositOptions
        fields = '__all__'
```
product = DepositProductsSerializer()는 DepositOptionsSerializer의 필드 중 하나로, DepositOptions 모델의 product 필드를 DepositProductsSerializer를 통해 직렬화하고자 함을 의미합니다.  

이렇게 함으로써 DepositOptions 모델의 각 인스턴스에 대해 product 필드가 DepositProductsSerializer를 통해 직렬화되어 표현될 것입니다.   
  
즉, DepositOptionsSerializer를 통해 조회할 때 product 필드의 값은 DepositProductsSerializer를 통해 정의된 형식으로 반환됩니다.

  
4. 가장 오래걸렸던 과제는 A. 정기예금 상품 목록 DB 저장이었습니다.
처음 product는 잘 저장이 되었지만, option 부분이 저장이 되지 않아 시간이 오래 걸렸습니다. 또한 unique=True 를 설정하지 않아 중복된 데이터가 들어가기도 했습니다.

하지만 결국 이 코드를 통해 해결했습니다.

```python
for product in DepositProducts.objects.filter(fin_prdt_cd = save_deposit_products['fin_prdt_cd']):
            save_deposit_products['product'] = product.pk

```

orm에서 filter는 sql문의 where와 비슷하다는 걸 배웠습니다.  
또한 E 과제를 진행하면서, 장고도 sql문에서의 order by를 사용할 수 있다는 점을 배웠습니다.

```python
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
```

이처럼 order_by와 - 를 통해 내림차순으로 정렬할 수 있었습니다.  

또한 refetch_related로 prefetch_related를 사용하여 쿼리를 최적화하면 데이터베이스 부하를 줄이고 프로젝트의 성능을 향상시킬 수 있습니다.


&nbsp;


## 윤채연

- A. 정기예금 상품 목록 및 옵션 목록 저장

*  정기예금 API 로부터 전달받은 데이터 중 상품 목록 정보와 옵션 목록 정보를 DB 에 저장

* 핵심 code :

    ```py
    ### 0. 해당 API 구조 파악 !
    # 1. API를 받아오는 url을 작성하여, 전체 데이터를 잘 받아오는 지 확인함
    def index(request):
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    
    # 2. JOSN 형식으로 바꿔서 resoponse에 넣어줌
    response = requests.get(url).json()
    
    return JsonResponse(response, safe=False)

    # 3. API 구조에 따른 세부 코드 작성 필요
    # 상품정보와 옵션 정보를 추출하는 데 구조가 다르기에, 파악 후 추출 가능
    baseListresponse = response['result']['baseList']
    optionListresponse = response['result']['optionList']

    ### 1. 옵션 목록 정보와 상품 모델 키의 관계 !
    # 1. 상품 목록에 있는 코드와 옵션 목록에 있는 코드가 동일하다면,
    for product in DepositProducts.objects.filter(fin_prdt_cd = save_deposit_products['fin_prdt_cd']):
        # 2. 해당 상품의 primary key를 옵션 목록 정보 모델의 product 필드에 값을 부여
        save_deposit_products['product'] = product.pk

    serializer = DepositOptionsSerializer(data=save_deposit_products)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    
    break

    ```

* 결과 :
  
  * 필요한 정기 상품 목록 및 옵션 목록을 추출하기 위해서는 단순url이 담긴 response를 출력하면 되는 것이 아닌, `API 구조를 파악`하고 해당 데이터가 담긴 구조에 위치한 데이터를 출력하는 것이 핵심 부분이었다고 생각합니다. 

  * 또한, `외래키`를 가져오기 위한 과정에서 상품 목록과 옵션 목록 정보에 동일하게 있는 상품코드를 바탕으로 관계를 파악하고, 해당 primary key를 찾아 옵션 목록의 product 필드에 정보를 넣어주는 것도 핵심 부분이었다고 생각합니다.
-----

- D. 특정 상품의 옵션 리스트 출력

* 아래 URL 로 요청이 오면 상품 코드에 따라 해당 상품의 옵션 리스트를 출력하도록 코드를 구현

* 핵심 code :

    ```py
    ### API는 GET요청을 처리할 수 있음 !
    @api_view(['GET'])
    # 1. 해당하는 금융 상품 코드를 가진 입금 옵션들을 검색하고 응답을 반환함
    def deposit_products_options(request, fin_prdt_cd):
        if request.method == 'GET':
            db = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
            serializer = DepositOptionsSerializer(db, many=True)
            return Response(serializer.data)
    ```

* 결과 :
    * Django REST framework를 사용하여 작성된 api_view로, `GET`요청을 처리하여 fin_prdt_cd에 해당하는 금융 상품 코드를 가진 옵션들을 검색하는 것이 핵심 부분이었다고 생각합니다.

-----
- E. 금리가 가장 높은 상품의 정보 출력

*  저축 기간에 상관 없이, “최고 우대 금리” 가 가장 높은 상품의 정보와 옵션 리스트를 반환

* 핵심 code :
    ```py
    ### API는 GET요청을 처리할 수 있음 !
    @api_view(['GET'])
    # 1. 최고 금리를 추출하기 위한 '-' + order_by 정렬로, 내림차순으로 정렬 한 뒤 가장 첫번째 값을 max_rate_product에 넣음
    def top_rate(request):
        if request.method == 'GET':
            max_rate_product = DepositOptions.objects.prefetch_related('product').order_by('-intr_rate2')[0]
            serializer = DepositOptionsSerializer(max_rate_product)
            return Response(serializer.data)
    ```

    ```py
    ### serializers.py에 추가한 code !
    # DepositOptions 모델에 있는 product 필드를 serializer하기 위해 작성
    product = DepositProductsSerializer()

    ```

    ```sql
    <!-- 위의 코드와 동일한 sql code -->
    SELECT * FROM DepositOptions
    
    INNER JOIN DepositProducts
    
    ON DepositOptions.product = DepositProducts.fin_prdt_cd;
    
    ```

* 결과:
    * 최고 우대 금리를 추출하기 위해서  `order_by`사용과 내림차순 정렬을 위한 필드 앞에 `-`붙여 해당 데이터를 추출하는 것이 핵심 부분이었다고 생각합니다.
    * 또한, 해당하는 옵션의 정보와 상품 정보까지 추출하기 위해서 `serializers.py`에서 두 모델의 관계를 담는 코드를 추가하고, `prefetch_related`를 통해 외래키로 연결된 객체를 가져오는 것이 핵심 부분이었다고 생각합니다.

-----
<br>

### 배운점
* API를 불러오는 것부터, 구조를 파악하여 내가 원하는 데이터를 추출하는 방법에 대해 알 수 있었습니다.

* 추가로, 해당 API를 불러와 DB에 저장하고 여러 모델 간의 관계를 만들고 활용하여 데이터를 추가, 추출하는 법에 대해 집중으로 배울 수 있는 프로젝트라 무엇보다도 유익했습니다 !
