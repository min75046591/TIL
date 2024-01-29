# PJT 01

### 이번 pjt 를 통해 배운 내용

* api 를 가져와 내가 필요한 정보를 추출해내는 방법을 배웠다.

* 새로운 리스트를 만들어 내가 원하는 정보를 넣는 것을 배웠다.

* json 형식으로 데이터 변환

* pprint를 사용하면 깔끔한 답을 추출 해낼 수 있다.
---

## A. 데이터 추출 - Key 값 출력하기

* 요구 사항 : 전체 정기예금의 응답을 json 형태로 변환 후 아래와 같이 Key 값만 출력하도록 구성하기
* 결과 : dict_keys(['prdt_div', 'total_count', 'max_page_no', 'now_page_no', 'err_cd', 'err_msg', 'baseList', 'optionList'])
  
  ```python
  def get_deposit_products():
  # 본인의 API KEY 로 수정합니다.
  api_key = '64707c0cf5710d008e3f7986f61f3099'
  url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
  # 요구사항에 맞도록 이곳의 코드를 수정합니다.
  result = requests.get(url).json()
  result = result['result'].keys()
  return result 
  ```
  
  * 이 문제에서 어려웠던점 : api 발급 받는 사이트가 같은 금융감독원인데 살짝다르다고 api 발급이 잘 안됐다.
  * 내가 생각하는 이 문제의 포인트 : api_key와 필요한 데이터의 url을 잘 넣고 데이터를 json으로 변환시키고 'result'를 .keys()로 뽑기

## B. 데이터 추출 - 전체 정기예금 상품 리스트

* 요구 사항 : 응답 중 정기예금 상품 리스트 정보만 출력하도록 구성

* 결과 : {'dcls_end_day': None,
  'dcls_month': '202312',
  'dcls_strt_day': '20231220',
  'etc_note': '- 1인 1계좌\n- 최저 100만원 이상',
  'fin_co_no': '0014807',
  'fin_co_subm_day': '202312200918',
  'fin_prdt_cd': '10120110400011',
  'fin_prdt_nm': 'Sh평생주거래우대예금\n(만기일시지급식)',        
  'join_deny': '1',
  'join_member': '실명의 개인',
  'join_way': '영업점',
  'kor_co_nm': '수협은행',
  'max_limit': None,
  'mtrt_int': '* 만기후 1년 이내\n'
              ' - 만기당시 일반정기예금(월이자지급식) 계약기간별  
기본금리 1/2\n'
              '* 만기후 1년 초과\n'
              ' - 만기당시 보통예금 기본금리',
  'spcl_cnd': '* 최대우대금리 : 0.4%\n'
              '1. 거래고객우대금리 : 최대0.1% (신규시) \n'        
              ' -최초예적금고객/재예치/장기거래 각 0.05% \n'      
              '2. 거래실적우대금리 : 최대0.3% (만기시)\n'
              ' -급여,연금이체등/수협카드결제/공과금이체등 각0.1%\n'
              '※단위:연%p'},
  
  ```python
  result = result['result']['baseList']
  ```
  

  * 내가 생각하는 이 문제의 포인트 : key 값이 'result'인 데이터를 출력 후 그 데이터에서 key 값이 'baseList'인 데이터를 출력하는 것


## C. 데이터 가공 - 전체 정기예금 옵션 리스트

* 요구 사항 : 응답 중 정기 예금 상품들의 옵션 리스트를 출력하도록 구성. 이 때, 원하는 데이터만 출력되는 결과를 반환하는 함수를 통해 작성

* 결과 : [{'금융상품코드': 'WR0001B',
  '저축 금리': 3,
  '저축 기간': '1',
  '저축금리유형': 'S',
  '저축금리유형명': '단리',
  '최고 우대금리': 3},
 {'금융상품코드': 'WR0001B',
  '저축 금리': 3.6,
  '저축 기간': '3',
  '저축금리유형': 'S',
  '저축금리유형명': '단리',
  '최고 우대금리': 3.6},
  ~~
  ```python
  result = result['result']['optionList']
  
  
  dict_list = []
  for i in result:
     new_dict = {}
     new_dict['금융상품코드'] = i['fin_prdt_cd']
     new_dict['저축 금리'] = i['intr_rate']
     new_dict['저축 기간'] = i['save_trm']
     new_dict['저축금리유형'] = i['intr_rate_type']
     new_dict['저축금리유형명'] = i['intr_rate_type_nm']
     new_dict['최고 우대금리'] = i['intr_rate2']
     dict_list.append(new_dict)
  
  return dict_list
  ```
  
  * 이 문제에서 어려웠던점 : 새로운 리스트 안에 딕트를 만들고 key 이름을 바꾸는게 어려웠다
  * 내가 생각하는 이 문제의 포인트 : 위 와 동일함


## D. 데이터 가공 -새로운 값을 만들어 반환하기

* 요구 사항 : 상품과 옵션 정보들을 담고 있는 새로운 값을 만들어 딕셔너리 형태로 반환하도록 구성.

* 결과 :  [{'저축 금리': 2.95,
            '저축 기간': 3.2,
            '저축금리유형': 'S',
            '저축금리유형명': '단리',
            '최대 우대금리': '36'},
           {'저축 금리': 3.55,
            '저축 기간': 3.8,
            '저축금리유형': 'S',
            '저축금리유형명': '단리',
            '최대 우대금리': '6'},
           {'저축 금리': 3.6,
            '저축 기간': 3.85,
            '저축금리유형': 'S',
            '저축금리유형명': '단리',
            '최대 우대금리': '12'}],
  '금융상품명': '토스뱅크 먼저 이자 받는 정기예금',
  '금융회사명': '토스뱅크 주식회사'}]
  
  ```python
   result_len = len(result['result']['baseList'])

    result_opt = result['result']['optionList'][0]['fin_co_no']

    result_main = result['result']['baseList'][0]['fin_co_no']


    value = []
    for i in range(result_len):
        if result_opt == result_main:
        
            value.append({'저축 금리' : result['result']['optionList'][i]['intr_rate'], '저축 기간' : result['result']['optionList'][i]['intr_rate2'], '저축금리유형' : result['result']['optionList'][i]['intr_rate_type'], '저축금리유형명' : result['result']['optionList'][i]['intr_rate_type_nm'], '최대 우대금리' : result['result']['optionList'][i]['save_trm']})

    info = []

    for i in range(len(value)):
    
        info.append({'금리정보' : value, '금융상품명' : result['result']['baseList'][i]['fin_prdt_nm'], '금융회사명' : result['result']['baseList'][i]['kor_co_nm']})

    pprint.pprint(info)  
  ```
  
  * 이 문제에서 어려웠던점 : 문제를 이해하고 코드를 구현하는데 도움이 없었다면 해결할 수 없었다. 그만큼 어려웠고 아무것도 없는 상태에서도 할 수 있을 정도로 코드를 분석 해야겠다는 생각이 들었다.
  * 내가 생각하는 이 문제의 포인트 : 옵션리스트와 베이스리스트를 새로운 변수로 할당해주고 value = []를 먼저 만들고 그 안에 info = []를 넣어서 정보를 추가해주는게 포인트라 생각함.



# 후기

* 나의 부족함을 너무나 크게 느꼈다.
* 나는 집가서 보상이 아닌 회초리를 때려야겠다.
* 나를 죽이지 못하는 고통은 나를 더 강하게 만든다.
* 다른 사람에 비해 지금은 부족한 나지만 지금 고통을 견디고 버티면
* 누구보다 단단한 내가 될거라 믿는다.
* 안되면 처음부터 다시 시작해보자.
* 모든것은 기본에서 시작한다. -손웅정-
